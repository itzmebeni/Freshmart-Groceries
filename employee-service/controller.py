from flask import request, jsonify

# No need to initialize PyMongo here. We'll use the one from app.py

def create_employee(mongo):
    data = request.get_json()
    # Validation for required fields
    required_fields = ['fullname', 'dob', 'address', 'contact_number', 'emergency_contact']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    employee = {
        'fullname': data['fullname'],
        'dob': data['dob'],
        'address': data['address'],
        'contact_number': data['contact_number'],
        'emergency_contact': data['emergency_contact']
    }

    employee_id = mongo.db.employees.insert_one(employee).inserted_id
    return jsonify({"message": "Employee created", "id": str(employee_id)}), 201

def get_all_employees(mongo):
    employees = mongo.db.employees.find()
    employee_list = []
    for employee in employees:
        employee['_id'] = str(employee['_id'])  # Convert ObjectId to string
        employee_list.append(employee)
    return jsonify(employee_list)

def get_employee(employee_id, mongo):
    employee = mongo.db.employees.find_one({'_id': employee_id})
    if employee:
        employee['_id'] = str(employee['_id'])
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404
