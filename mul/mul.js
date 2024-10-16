const express = require('express');
const app = express();
const port = 5000;

// Middleware to parse JSON request body
app.use(express.json());

// POST endpoint for multiplication
app.post('/api/mul', (req, res) => {
    const { number1, number2 } = req.body;

    // Check if numbers are provided
    if (number1 == null || number2 == null) {
        return res.status(400).json({ error: 'Please provide both numbers' });
    }

    // Perform multiplication
    const result = number1 * number2;

    // Return the result
    res.json({ result });
});

// Start the server
app.listen(port, () => {
    console.log(`Multiplication service running at http://localhost:${port}`);
});
