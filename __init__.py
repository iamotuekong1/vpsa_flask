from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.resources.user import UserRegister, UserLogin
from app.resources.product import ProductList
from app.controllers.recommendation_engine import Recommendation
from app.controllers.search_engine import Search

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    api = Api(app)
    jwt = JWTManager(app)

    # Register routes (API Gateway)
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(ProductList, '/products')
    api.add_resource(Recommendation, '/recommendation')
    api.add_resource(Search, '/search')

    return app
