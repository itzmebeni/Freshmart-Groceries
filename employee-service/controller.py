from flask import Blueprint
from model import create_employee, get_all_employees, get_employee

employee_bp = Blueprint('employee_bp', __name__)

# Route to create a new employee
employee_bp.route('/employees', methods=['POST'])(create_employee)

# Route to get all employees
employee_bp.route('/employees', methods=['GET'])(get_all_employees)

# Route to get a specific employee by ID
employee_bp.route('/employees/<employee_id>', methods=['GET'])(get_employee)
