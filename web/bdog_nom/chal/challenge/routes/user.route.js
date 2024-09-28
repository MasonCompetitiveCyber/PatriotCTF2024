const express = require("express");
const User = require("../models/Users");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const userRoutes = express.Router();
const { JWT_SECRET } = require("../constant");
const { authMiddleware } = require("../middleware");

// User registration
userRoutes.post("/register", async (req, res) => {
  let { username, firstName, lastName, password } = req.body;
  if (
    typeof username !== "string" ||
    typeof firstName !== "string" ||
    typeof lastName !== "string"
  ) {
    return res.status(400).json({ message: "Invalid format" });
  }
  try {
    // Check if username already exists
    let user = await User.findOne({
      username: String(username),
    });
    if (user) {
      return res.status(400).json({ message: "User already exists" });
    }
    if (username.trim().length < 3) {
      return res
        .status(400)
        .json({ message: "Username must be at least 3 characters." });
    }
    if (firstName.trim().length < 1 || lastName.trim().length < 1) {
      return res.status(400).json({
        message: "First name and Last name must be at least 1 character.",
      });
    }
    // Create new user
    user = new User({
      username: String(username),
      firstName: String(firstName),
      lastName: String(lastName),
      role: "user",
      password: await bcrypt.hash(String(password), 10),
    });

    await user.save();
    res.json({ message: "User registered successfully" });
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
});

// User login
userRoutes.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    // Check if user exists
    const user = await User.findOne({ username: String(username) });
    if (!user) {
      return res.status(400).json({ message: "Invalid credentials" });
    }

    const isMatch = await bcrypt.compare(String(password), user.password);
    if (!isMatch) {
      return res.status(400).json({ message: "Invalid credentials" });
    }

    // Create and send JWT token
    const token = jwt.sign({ userId: user._id }, JWT_SECRET, {
      expiresIn: "1h",
    });
    res.cookie("token", token, {
      httpOnly: true,
      secure: false,
      maxAge: 3600000,
    });
    res.status(200).redirect("/");
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
});

// Get User Profile
userRoutes.get("/", authMiddleware, async (req, res) => {
  const userId = String(req.user);
  const user = await User.find({ user: userId });
  res.json(user);
});

// TODO: make admin middleware
userRoutes.get("/:id", authMiddleware, async (req, res) => {
  if (!req.params.id) {
    return res.status(400).json({ message: "Missing id param" });
  }
  const searchId = String(req.params.id);
  const user = await User.find({ user: searchId });
  res.json(user);
});

module.exports = userRoutes;
