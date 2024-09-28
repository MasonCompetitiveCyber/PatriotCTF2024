#!/bin/bash

# Replace placeholders with environment variables in the MongoDB init script
sed -i "s/{{MONGO_USER}}/$MONGO_USER/g" /docker-entrypoint-initdb.d/mongo-init.js
sed -i "s/{{MONGO_PASSWORD}}/$MONGO_PASSWORD/g" /docker-entrypoint-initdb.d/mongo-init.js
sed -i "s/{{FLAG}}/$FLAG/g" /docker-entrypoint-initdb.d/mongo-init.js
sed -i "s#{{ADMIN_PASSWORD}}#$ADMIN_PASSWORD#g" /docker-entrypoint-initdb.d/mongo-init.js

# Start MongoDB in the background
mongod --bind_ip 127.0.0.1 --fork --logpath /dev/null --dbpath /data/db

# Wait until MongoDB is ready to accept connections
echo "Waiting for MongoDB to start..."
/usr/src/wait/wait-for-it.sh localhost:$MONGO_PORT -- mongosh < /docker-entrypoint-initdb.d/mongo-init.js

# Create the cron job for removing non-admin users and tasks every 10 minutes
echo "*/10 * * * * /usr/src/app/cleanup.sh >> /dev/null 2>&1" > /etc/cron.d/cleanup-cron
chmod 0644 /etc/cron.d/cleanup-cron
crontab /etc/cron.d/cleanup-cron

echo "Starting cron service..."
service cron start

# Start supervisor
echo "Starting supervisor..."
exec /usr/bin/supervisord -c /etc/supervisord.conf