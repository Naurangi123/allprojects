const mongoose = require("mongoose");

const tutorialSchema = new mongoose.Schema(
  {
    title: String,
    description: String,
    published: Boolean
  },
  { timestamps: true }
);


module.exports = mongoose.model("Tutorial", tutorialSchema);
