const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let User = new Schema({
	username: {
		type: String,
		required: true,
		unique: true
	},
	firstName: {
		type: String,
		required: true
	},
	lastName: { 
		type: String,
		required: true
	},
	role: {
		type: String,
		enum: ['user', 'admin'],
		default: 'user'
	},
	password: {
		type: String,
		required: true
	},
}, {
	collection: 'users'
});

module.exports = mongoose.model('User', User);