FROM php:7.2-fpm

RUN apt update -y

# Install dependencies
RUN apt -y  install supervisor \
    apache2 \
    libyaml-dev \ 
    cron

# Install PHP extensions
RUN pecl install yaml && echo "extension=yaml.so" > /usr/local/etc/php/conf.d/ext-yaml.ini && docker-php-ext-enable yaml

# Copy .htaccess file
COPY conf-files/.htaccess /var/www/html/

# create .htpasswd file
RUN htpasswd -bc /etc/apache2/.htpasswd admin noneedtobruteforce919151

# Copy files
COPY php-files/challenge.php /var/www/html/
COPY php-files/index.php /var/www/html/

# Copy apache configuration
COPY conf-files/000-default.conf /etc/apache2/sites-available/

# Copy supervisor configuration
COPY conf-files/php-fpm.conf /etc/supervisor/conf.d/
COPY conf-files/apache.conf /etc/supervisor/conf.d/
COPY conf-files/cron.conf /etc/supervisor/conf.d/

# Enable apache modules
RUN a2enmod rewrite \
            proxy \
            proxy_fcgi \
            auth_basic

# Remove default index.html
RUN rm /var/www/html/index.html

# Remove all files except index.php, challenge.php and .htaccess
RUN \
    echo "find /var/www/html ! \( -iname 'index.php' -o -iname 'challenge.php' -o -iname '.htaccess' \) -type f -exec rm -f {} + " > /root/script.sh \
    && echo "echo PCTF{Kiran_SAU_Manifested} > /get-here/flag.txt" >> /root/script.sh \
    && chmod +x /root/script.sh

# Add crontab file in the cron directory
# Run cron job every 30 seconds
COPY conf-files/crontab /etc/crontab

# Give execution rights on the cron job
RUN chmod 0644 /etc/crontab
RUN crontab /etc/crontab


# Flag location
RUN mkdir /get-here \
    && echo "PCTF{Kiran_SAU_Manifested}" > /get-here/flag.txt

# Change ownership
RUN chown -R www-data:www-data /get-here

# Expose port 80
EXPOSE 80

# Start supervisord
CMD ["/usr/bin/supervisord", "-n"]
