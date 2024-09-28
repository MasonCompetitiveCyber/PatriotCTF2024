# sudo docker build -t dogdays .
# sudo docker run -dp 7777:80 dogdays:latest

FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y \
    && apt install php -y \
    && apt install apache2 -y \
    && apt install supervisor -y

# Switch working environment
WORKDIR /var/www/html
RUN rm /var/www/html/index.html

# COPY challenge
COPY challenge .
COPY flag /flag

# Changing Ownership
RUN chown -R www-data: /var/www/html
RUN chown www-data: /flag

RUN service apache2 restart

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

# Run as low-level user
RUN useradd -m ctf
RUN sed -i -e 's/APACHE_RUN_USER=www-data/APACHE_RUN_USER=ctf/g' /etc/apache2/envvars
RUN sed -i -e 's/APACHE_RUN_GROUP=www-data/APACHE_RUN_GROUP=ctf/g' /etc/apache2/envvars
ENV APACHE_RUN_USER=ctf
ENV APACHE_RUN_GROUP=ctf
RUN service apache2 restart

EXPOSE 80

CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]
