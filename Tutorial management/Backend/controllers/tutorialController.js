const Tutorial = require('../models/tutorialModel');

// Create and Save a new Tutorial
module.exports.create = async (req, res) => {
  try {
    if (!req.body.title) {
      return res.status(400).json({ message: "Title is required!" });
    }

    const tutorial = new Tutorial({
      title: req.body.title,
      description: req.body.description,
      published: req.body.published ?? false,
    });

    const data = await tutorial.save();
    res.status(201).json(data);
  } catch (err) {
    res.status(500).json({ message: err.message || "Error creating the Tutorial." });
  }
};

// Retrieve all Tutorials
module.exports.findAll = async (req, res) => {
  try {
    const data = await Tutorial.find({});
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ message: err.message || "Error retrieving tutorials." });
  }
};

// Find a single Tutorial with an id
module.exports.findOne = async (req, res) => {
  try {
    const id = req.params.id;
    const data = await Tutorial.findById(id);

    if (!data) {
      return res.status(404).json({ message: `Tutorial not found with id=${id}` });
    }

    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ message: "Error retrieving Tutorial with id=" + id });
  }
};

// Update a Tutorial by id
module.exports.update = async (req, res) => {
  try {
    if (!req.body) {
      return res.status(400).json({ message: "Data to update can not be empty!" });
    }

    const id = req.params.id;
    const data = await Tutorial.findByIdAndUpdate(id, req.body, { new: true, useFindAndModify: false });

    if (!data) {
      return res.status(404).json({ message: `Cannot update Tutorial with id=${id}. Tutorial not found!` });
    }

    res.status(200).json({ message: "Tutorial updated successfully." });
  } catch (err) {
    res.status(500).json({ message: "Error updating Tutorial with id=" + id });
  }
};

// Delete a Tutorial by id
module.exports.delete = async (req, res) => {
  try {
    const id = req.params.id;
    const data = await Tutorial.findByIdAndRemove(id, { useFindAndModify: false });

    if (!data) {
      return res.status(404).json({ message: `Cannot delete Tutorial with id=${id}. Tutorial not found!` });
    }

    res.status(200).json({ message: "Tutorial deleted successfully!" });
  } catch (err) {
    res.status(500).json({ message: "Could not delete Tutorial with id=" + id });
  }
};

// Delete all Tutorials
module.exports.deleteAll = async (req, res) => {
  try {
    const data = await Tutorial.deleteMany({});
    res.status(200).json({ message: `${data.deletedCount} Tutorials deleted successfully!` });
  } catch (err) {
    res.status(500).json({ message: err.message || "Error removing all tutorials." });
  }
};

// Find all published Tutorials
module.exports.findAllPublished = async (req, res) => {
  try {
    const data = await Tutorial.find({ published: true });
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ message: err.message || "Error retrieving published tutorials." });
  }
};
