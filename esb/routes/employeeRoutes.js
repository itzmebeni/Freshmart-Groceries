// employeeRoutes.js
const express = require('express');
const { createEmployee, getAllEmployees, getEmployee } = require('../controllers/employeeController');

const router = express.Router();

router.post('/', createEmployee);
router.get('/', getAllEmployees);
router.get('/:employee_id', getEmployee);

module.exports = router;