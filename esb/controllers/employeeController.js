const axios = require('axios');
const EMPLOYEE_SERVICE_URL = process.env.EMPLOYEE_SERVICE_URL;

// Create a new employee
const createEmployee = async (req, res) => {
    try {
        const response = await axios.post(`${EMPLOYEE_SERVICE_URL}/employees`, req.body);
        res.status(response.status).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ error: 'Internal Server Error' });
        }
    }
};

// Get all employees
const getAllEmployees = async (req, res) => {
    try {
        const response = await axios.get(`${EMPLOYEE_SERVICE_URL}/employees`);
        res.status(response.status).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ error: 'Internal Server Error' });
        }
    }
};

// Get a specific employee by ID
const getEmployee = async (req, res) => {
    try {
        const { employee_id } = req.params;
        const response = await axios.get(`${EMPLOYEE_SERVICE_URL}/employees/${employee_id}`);
        res.status(response.status).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ error: 'Internal Server Error' });
        }
    }
};

module.exports = { createEmployee, getAllEmployees, getEmployee };