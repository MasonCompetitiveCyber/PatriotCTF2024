db = db.getSiblingDB('dbog_nom');
db.createUser({
    user: "{{MONGO_USER}}",
    pwd: "{{MONGO_PASSWORD}}",
    roles: [
        {
            role: "readWrite",
            db: "dbog_nom"
        }
    ]
});

db.createCollection("config");
db.createCollection("users");

db.config.insertOne({
    value: '{{FLAG}}',
    type: 'flag'
})

db.users.insertOne({
    username: "admin",
    firstName: "Test",
    lastName: "Admin",
    role: "admin",
    password: "{{ADMIN_PASSWORD}}" 
})