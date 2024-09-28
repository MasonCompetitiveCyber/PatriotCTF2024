FROM python:3.11-alpine

# Install packages
RUN apk add --no-cache --update mariadb mariadb-client supervisor gcc musl-dev mariadb-connector-c-dev openssl

RUN python -m pip install --upgrade pip

RUN mkdir -p /app

# Setup supervisor
COPY --chown=root config/supervisord.conf /etc/supervisord.conf

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Install dependencies
RUN pip install -r requirements.txt

# Create www-data group and user
RUN adduser -S www-data -G www-data

# Changing Ownership
RUN chown -R www-data: /app /run

# Make sure run.py executable
RUN chmod +x /app/run.py

# # Disable pycache
# ENV PYTHONDONTWRITEBYTECODE=1

# # Disable pycache
# ENV PYTHONDONTWRITEBYTECODE=1


# MySQL Configurations
ENV MYSQL_HOST="localhost"
ENV MYSQL_USER="user"
ENV MYSQL_PASSWORD="Rea!!ytr)ngPassword829819818821812891282812981891"
ENV MYSQL_DB="door"
# Flag
ENV FLAG="pctf{str_f1rm4t_1s_k1nd8_c00l_7712817812}"

# Random Admin Password

# Expose port the server is reachable on
EXPOSE 1337

# create database and start supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]