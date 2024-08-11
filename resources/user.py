from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models import User

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400

        user = User(username=data['username'], password=data['password'])
        user.save_to_db()

        return {'message': 'User registered successfully'}, 201

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        user = User.find_by_username(data['username'])

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401
