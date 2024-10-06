const express = require('express');
const tutorials = require('../controllers/tutorialController');
const router = express.Router();

// Retrieve all tutorials
router.get('/', tutorials.findAll);

// Create a new tutorial
router.post('/', tutorials.create);

// Retrieve all published tutorials
router.get('/published', tutorials.findAllPublished);

// Retrieve a single tutorial by ID
router.get('/:id', tutorials.findOne);

// Update a tutorial by ID
router.put('/:id', tutorials.update);

// Delete a tutorial by ID
router.delete('/:id', tutorials.delete);

// Delete all tutorials
router.delete('/', tutorials.deleteAll);

module.exports = router;
