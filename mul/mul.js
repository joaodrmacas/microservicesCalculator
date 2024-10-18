const express = require('express');
const axios = require('axios'); // Import axios for making HTTP requests
const app = express();
const port = 5000;

// Middleware to parse JSON request body
app.use(express.json());

// Define the db-service URL as a global variable
const DB_SERVICE_URL = "http://db-service:5000/save";

// POST endpoint for multiplication
app.post('/api/mul', async (req, res) => {
    const { number1, number2 } = req.body;

    // Check if numbers are provided
    if (number1 == null || number2 == null) {
        return res.status(400).json({ error: 'Please provide both numbers' });
    }

    // Perform multiplication
    const result = number1 * number2;

    // Prepare data for the external POST request
    const saveData = {
        result: result,
        operation: 'multiplication'
    };

    try {
        // Make a POST request to the db-service
        await axios.post(DB_SERVICE_URL, saveData);
    } catch (error) {
        console.error('Error saving to db-service:', error.message);
        return res.status(500).json({ error: 'Failed to save result' });
    }

    // Return the result
    res.json({ result });
});

// Start the server
app.listen(port, () => {
    console.log(`Multiplication service running at http://localhost:${port}`);
});
