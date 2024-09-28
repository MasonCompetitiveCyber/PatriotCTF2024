FROM python

LABEL author="kiransau"

LABEL name="DOMDOM"

RUN apt update -y \
    && pip3 install flask  \
    && pip3 install requests \
    && pip3 install pillow \
    && pip3 install lxml \ 
    && apt install supervisor cron -y

# Copy flag
COPY flag.txt /app/flag.txt

# Setup app
RUN mkdir -p /app
RUN mkdir -p /app/uploads

# Switch working environment
WORKDIR /app

# COPY challenge
COPY challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Changing Ownership
RUN chown -R www-data: /app \
    && chmod -R 755 /app

# Crontab for /uploads
COPY clear_uploads.sh /root/clear_uploads.sh
RUN chown root: /root/clear_uploads.sh
RUN chmod 700 /root/clear_uploads.sh
RUN crontab -l | { cat; echo "*/5 * * * * bash /root/clear_uploads.sh"; } | crontab -

# Expose port the server is reachable on
EXPOSE 9090

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD cron && /usr/bin/supervisord -c /etc/supervisord.conf
