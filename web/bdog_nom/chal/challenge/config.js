let mongo_port = Number(process.env.MONGO_PORT) || 27017;
let mongo_host = process.env.MONGO_HOST || "localhost";
let mongo_db_name = process.env.MONGO_DATABASE || "dbog_nom";
let mongo_user = process.env.MONGO_USER || "ctfuser";
let mongo_password = process.env.MONGO_PASSWORD || "";

module.exports = {
	DB: `mongodb://${mongo_user}:${mongo_password}@${mongo_host}:${mongo_port}/${mongo_db_name}`
};