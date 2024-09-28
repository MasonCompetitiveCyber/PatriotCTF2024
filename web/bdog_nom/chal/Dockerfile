# Use Node.js official image as the base image
FROM node:20

RUN mkdir -p /usr/src/app

RUN cat /etc/os*release

# ?NOTE: for debug
# RUN touch /var/log/supervisor.log


# Set the working directory in the container
WORKDIR /usr/src/app

# Setup supervisor
COPY --chown=root config/supervisord.conf /etc/supervisord.conf

# Copy package.json and package-lock.json
COPY challenge/package*.json ./

# Install the application dependencies, including devDependencies
RUN npm install

# Copy the cleanup script into the container
COPY --chown=root cleanup.sh /usr/src/app/cleanup.sh
RUN chmod +x /usr/src/app/cleanup.sh

# Script to start MongoDB and Node.js app using the shell script
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create ctfuser group and user
RUN groupadd -r ctfuser
RUN adduser --system ctfuser --ingroup ctfuser
# ?NOTE: For debug add "/var/log"
RUN chown -R ctfuser:ctfuser /usr/src/app /run /usr/local/bin/npm /usr/local/bin/node

# Install MongoDB and supervisor
RUN apt-get update && \
    apt-get install -y gnupg supervisor cron && \
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && \
    apt-get install -y mongodb-org && \
    mkdir -p /data/db

# MongoDB Config
ENV MONGO_PORT=27017
ENV MONGO_HOST="localhost"
ENV MONGO_DATABASE="dbog_nom"
ENV MONGO_USER="ctfuser"
# TODO: Change these env for chall (DONE):
ENV MONGO_PASSWORD="tuEQkpoJIF5uRBIrcab7"
ENV NODE_ENV="production"
ENV ADMIN_PASSWORD="\$2a\$10\$1OioM.ODWAD5SnmQ05kcguth03LTVV49cnxx78bnV1DuT5PMCtK9a"
ENV FLAG="pctf{bd_nom_nom_nom_n0m_nom_nom_819211278}"

# Copy the MongoDB initialization template and shell scripts
COPY --chown=root ./config/mongo-init.js /docker-entrypoint-initdb.d/mongo-init.js

# wait-for-it.sh script
COPY config/wait-for-it.sh /usr/src/wait/wait-for-it.sh
RUN chmod u+x /usr/src/wait/wait-for-it.sh

# Copy the rest of your application code into the container
COPY challenge/ .

# Expose the port your app runs on
EXPOSE 3000

ENTRYPOINT ["/entrypoint.sh"]

