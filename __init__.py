from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.resources.user import UserRegister, UserLogin
from app.resources.product import ProductList
from app.controllers.recommendation_engine import Recommendation
from app.controllers.search_engine import Search
from app.models import db  # Import the database instance

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Set up the database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary warnings

    api = Api(app)
    jwt = JWTManager(app)
    db.init_app(app)  # Initialize the database with the app

    # Register routes (API Gateway)
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(ProductList, '/products')
    api.add_resource(Recommendation, '/recommendation')
    api.add_resource(Search, '/search')

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
