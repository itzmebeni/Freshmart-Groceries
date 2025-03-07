from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from controller import create_employee, get_all_employees, get_employee  # Import functions

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Configuring MongoDB URI and port from the environment
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["PORT"] = int(os.getenv("PORT"))

# Initialize the PyMongo extension with the app
mongo = PyMongo(app)

# Debug message to confirm the connection
try:
    mongo.db.command('ping')
    print("MongoDB connected successfully!")
except Exception as e:
    print(f"MongoDB connection failed: {e}")

# Register the routes (Blueprints)
@app.route("/employees", methods=["POST"])
def add_employee():
    return create_employee(mongo)  # Pass mongo to the function

@app.route("/employees", methods=["GET"])
def list_employees():
    return get_all_employees(mongo)  # Pass mongo to the function

@app.route("/employees/<employee_id>", methods=["GET"])
def get_single_employee(employee_id):
    return get_employee(employee_id, mongo)  # Pass mongo to the function

# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])
