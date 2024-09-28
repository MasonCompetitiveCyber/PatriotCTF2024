const jwt = require("jsonwebtoken");
const { JWT_SECRET } = require("../constant");

// Middleware to authenticate users using JWT
const authMiddleware = (req, res, next) => {
  const token = req.cookies.token;
  if (!token) {
    return res.status(401).redirect('/login');
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded.userId;
    next();
  } catch (err) {
    return res.status(401).redirect('/login');
  }
};

module.exports = { authMiddleware };
