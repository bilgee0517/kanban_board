from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Load the application configuration from an external class
app.config.from_object(Config)

# Set the JWT Secret Key for token encoding/decoding
app.config['JWT_SECRET_KEY'] = 'secret'  # It's crucial to keep this key secret in a real application

# Enable Cross-Origin Resource Sharing (CORS) for frontend communication
CORS(app, supports_credentials=True)

# Initialize SQLAlchemy for ORM-based database interactions
db = SQLAlchemy(app)

# Initialize JWT Manager for handling JSON Web Tokens
jwt = JWTManager(app)

# Initialize Flask-RESTx API for easy REST API creation, documentation, and versioning
api = Api(app, version='1.0', title='Task API', description='A simple Task Management API')

# Import the namespaces from the resources modules
from resources.tasks import ns as tasks_ns
from resources.users import user_ns as users_ns
from resources.columns import ns as column_ns 

# Register the imported namespaces with the API to define the application's routes
api.add_namespace(tasks_ns, path='/tasks')  # Routes for task-related operations
api.add_namespace(users_ns, path='/users')  # Routes for user-related operations
api.add_namespace(column_ns, path='/columns')  # Routes for column-related operations

# Ensure the database tables are created based on defined models
with app.app_context():
    db.create_all()

# Run the application if this script is executed as the main program
if __name__ == '__main__':
    app.run(debug=True)  # Note: debug=True is for development purposes only
