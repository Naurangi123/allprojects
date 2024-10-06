require('dotenv').config(); 
const express = require("express");
const bodyParser = require('body-parser');
const cors = require("cors");
const path = require("path");
const tutorialRoutes = require("./routes/tutorialRoutes");
const mongoose = require('mongoose');

const app = express();

// CORS Configuration
app.use(cors({
  origin: "http://localhost:3000", // Update this with your front-end URL
}));

// Middleware
app.use(express.json());
app.use(bodyParser.json()); 

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// API Routes
app.use("/api/tutorials", tutorialRoutes); // Prefix API routes

// Start server
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
