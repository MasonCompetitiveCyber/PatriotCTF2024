const express = require("express");
const Task = require("../models/Task");
const taskRoutes = express.Router();
const { authMiddleware } = require("../middleware");
const { DISABLED_OPERATION_MONGO } = require("../constant");

// Get all tasks for the logged-in user
taskRoutes.get("/", authMiddleware, async (req, res) => {
  const userId = String(req.user);
  const tasks = await Task.find({ user: userId });
  res.json(tasks);
});

// Add a new task for the logged-in user
taskRoutes.post("/", authMiddleware, async (req, res) => {
  const userId = String(req.user);
  if (!req.body.title) {
    return res.status(400).json({ message: "Missing title" });
  }
  const newTask = new Task({
    title: String(req.body.title),
    user: userId,
  });
  const task = await newTask.save();
  res.json(task);
});

// Update a task (mark as completed) for the logged-in user
taskRoutes.put("/:id", authMiddleware, async (req, res) => {
  const userId = String(req.user);
  if (!req.body.id) {
    return res.status(400).json({ message: "Missing id" });
  }
  if (!req.body.completed || typeof req.body.completed !== "boolean") {
    return res.status(400).json({ message: "Missing completed status" });
  }
  const task = await Task.findOneAndUpdate(
    { _id: String(req.params.id), user: userId },
    { completed: Boolean(req.body.completed) },
    { new: true }
  );
  if (!task) {
    return res.status(404).json({ message: "Task not found" });
  }
  res.json(task);
});

taskRoutes.get("/search", authMiddleware, async (req, res) => {
  try {
    const filter = req.body.filter;
    if (!filter || typeof filter !== "object") {
      return res.status(400).json({ message: "Missing filter" });
    }
    if (Array.isArray(filter)) {
      return res.status(400).json({ message: "Invalid filter" });
    }
    const filterKeys = Object.keys(filter);
    if (Object.keys(filter).length > 5) {
      return res.status(400).json({ message: "Too many filter options" });
    }
    let foundDisabledKey = false;
    for (let i = 0; i < filterKeys.length; i++) {
      let k = filterKeys[i];
      if (DISABLED_OPERATION_MONGO.includes(k)) {
        foundDisabledKey = true;
        break;
      }
    }
    if (foundDisabledKey === true) {
      return res.status(400).json({ message: "Invalid Filter found" });
    }
    const updatedFilter = limitObjectDepth(filter, 2, 0);
    console.log(updatedFilter);
    Task.aggregate([updatedFilter, { $limit: 1 }])
      .then((t) => {
        res.json(t);
      })
      .catch((err) => {
        console.log(err);
        res.status(500).json({ message: "Something went wrong" });
      });
  } catch (err) {
    console.log(err);
    res.status(500).json({ message: "Something went wrong" });
  }
});

function limitObjectDepth(obj, maxDepth, currentDepth = 0) {
  if (currentDepth > maxDepth) {
    return;
  }
  if (Array.isArray(obj) || typeof obj !== "object" || obj === null) {
    // not an object
    return obj;
  }
  const result = {};
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      let val = limitObjectDepth(obj[key], maxDepth, currentDepth + 1);
      if (val) {
        result[key] = val;
      }
    }
  }
  if (Object.keys(result).length === 0) return;
  return result;
}

module.exports = taskRoutes;
