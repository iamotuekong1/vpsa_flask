from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models import UserInteraction  # Assuming you have a User model

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        # Logic to save the user to the database (not shown here)
        # Assuming user.save_to_db()

        return {'message': 'User registered successfully'}, 201

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        # Logic to authenticate the user (not shown here)
        # Assuming user = User.find_by_username(data['username'])

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200
