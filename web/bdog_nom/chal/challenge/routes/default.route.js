const express = require("express");
const defaultRoutes = express.Router();
const { authMiddleware } = require("../middleware");

defaultRoutes.route("/login").get(function (req, res) {
  res.render("login"); 
});

defaultRoutes.route("/register").get(function (req, res) {
  res.render("register"); 
});

defaultRoutes.route("/").get(authMiddleware, function (req, res) {
  res.render("index");
});



module.exports = defaultRoutes;
