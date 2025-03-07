require('dotenv').config(); // Load environment variables

const express = require('express');

// Import Routes
const productServices = require('./routes/inventory-route');
const posServices = require('./routes/pos-routes');
const authService = require('./routes/auth-routes');
const employeeServices = require('./routes/employeeRoutes'); // Employee Routes

// Request mapper
const mapper = '/api/v1';

// Init app
const app = express();

// Middleware
app.use(express.json());
app.use((req, res, next) => {
    console.log(`[${req.method}] ${req.path}`);
    next();
});

// Routes
app.use(`${mapper}/inventory`, productServices);
app.use(`${mapper}/pos`, posServices);
app.use(`${mapper}/auth`, authService);
app.use(`${mapper}/employees`, employeeServices); // Employee API route

// Default Route (Root)
app.get('/', (req, res) => {
    res.send({ message: 'Welcome to the API!' });
});

// 404 Handler for Undefined Routes
app.use((req, res) => {
    res.status(404).json({ error: 'No such endpoint exists' });
});

// Start the Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
});
