#!/bin/bash

# Remove all non-admin users and all tasks
mongosh --eval "
db = db.getSiblingDB('dbog_nom');
db.users.deleteMany({ role: { \$ne: 'admin' } });
db.tasks.deleteMany({});
"
