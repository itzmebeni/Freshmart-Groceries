
from flask import Blueprint, request, jsonify
from models.employee import Employee

employee_routes = Blueprint("employee_routes", __name__)

# Dummy in-memory storage (use database in real apps)
employees = []

@employee_routes.route("/employees", methods=["POST"])
def add_employee():
    """Endpoint to add a new employee."""
    data = request.json
    new_employee = Employee(
        data["full_name"],
        data["date_of_birth"],
        data["address"],
        data["contact_number"],
        data["emergency_contact"]
    )
    employees.append(new_employee)
    return jsonify({"message": "Employee added successfully", "employee": new_employee.to_dict()}), 201

@employee_routes.route("/employees", methods=["GET"])
def get_employees():
    """Endpoint to retrieve all employees."""
    return jsonify([emp.to_dict() for emp in employees]), 200
