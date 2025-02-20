

from flask import Flask
from routes.employee_routes import employee_routes

app = Flask(__name__)

# Register Blueprints (Routes)
app.register_blueprint(employee_routes)

if __name__ == "__main__":
    app.run(debug=True)
