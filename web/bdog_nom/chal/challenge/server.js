const express = require("express");
const bodyParser = require("body-parser");
const cookieParser = require('cookie-parser');
const mongoose = require("mongoose");
const config = require("./config");

const userRoute = require("./routes/user.route");
const tasksRoute = require("./routes/tasks.route");
const defaultRoute = require("./routes/default.route");

const app = express();

app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static("static"));
app.set("view engine", "ejs");

// Routes
app.use("/api/v0/user", userRoute);
app.use("/api/v0/tasks", tasksRoute);
app.use("/", defaultRoute);

mongoose.Promise = global.Promise;

mongoose
  .connect(config.DB)
  .then(() => {
    console.log("CONNECTED TO MONGODB");
    // Store the db connection in app.locals
    app.locals.db = mongoose.connection.db;
    let port = process.env.PORT || 3000;
    app.listen(port, function () {
      console.log("Listening on port " + port);
    });
  })
  .catch((err) => {
    console.error("FAILED TO CONNECT TO MONGODB");
    console.error(err);
  });
