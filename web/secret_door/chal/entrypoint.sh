#!/bin/sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --bind-address=127.0.0.1 --port=3306 --user=mysql --console --skip-networking=0 &
# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo 'not up' && sleep .2; done

# password length must be more than or equal to -c Number
function getEnvPW(){
    echo -n "$(openssl rand -base64 32 | sha256sum | head -c 64)"
}

# Generate passwords
ADMIN_PASSWORD=$(getEnvPW)

mysql -u root << EOF
CREATE DATABASE door;

USE door;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'regular') DEFAULT 'regular'
);

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    log_text TEXT NOT NULL,
    log_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO
    users (email, password, role)
VALUES
    ('admin@competitivecyber.club', '${ADMIN_PASSWORD}', 'admin');

DELIMITER //
CREATE PROCEDURE insert_user (
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    INSERT INTO users (email, password) VALUES (p_email, p_password);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE update_user_email (
    IN p_old_email VARCHAR(255),
    IN p_new_email VARCHAR(255)
)
BEGIN
    -- Check if the new email is already in use
    IF EXISTS (SELECT 1 FROM users WHERE email = p_new_email) THEN
        -- Throw an error indicating the email is already in use
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The new email address is already in use.';
    ELSE
        -- Update email if not in use
        UPDATE users
        SET email = p_new_email
        WHERE email = p_old_email;
    END IF;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE insert_log (
    IN p_user_email VARCHAR(255),
    IN p_log_text TEXT
)
BEGIN
    DECLARE v_user_id INT;

    -- Retrieve user_id based on p_user_email
    SELECT id INTO v_user_id
    FROM users
    WHERE email = p_user_email;

    -- Check if user_id was found
    IF v_user_id IS NOT NULL THEN
        -- Insert log entry if user_id was found
        INSERT INTO logs (user_id, log_text) VALUES (v_user_id, p_log_text);
    ELSE
        -- Handle case where email does not exist (optional)
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User not found for the given email.';
    END IF;
END //
DELIMITER ;

CREATE USER 'user'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';

GRANT EXECUTE ON PROCEDURE door.insert_user TO 'user'@'localhost';
GRANT EXECUTE ON PROCEDURE door.update_user_email TO 'user'@'localhost';
GRANT EXECUTE ON PROCEDURE door.insert_log TO 'user'@'localhost';

GRANT SELECT, INSERT ON door.users TO 'user'@'localhost';
GRANT SELECT, INSERT ON door.logs TO 'user'@'localhost';

FLUSH PRIVILEGES;
EOF

# Start supervisor
exec /usr/bin/supervisord -c /etc/supervisord.conf
