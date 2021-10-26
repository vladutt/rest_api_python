from flask_restful import Resource, reqparse
from source.Models.UserModel import UserModel
import re


class CreateUser(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help="Username field is required", type=str, required=True)
        parser.add_argument('password', help="Password field is required", type=str, required=True)
        parser.add_argument('email', help="Email field is required", type=str, required=True)
        args = parser.parse_args(strict=True)

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, args.email):
            return {'email': 'Please check your email format.'}

        if UserModel.checkUserIfExists(args.email):
            return {'email': 'Already exists'}

        user = UserModel(args.username, args.email, args.password)
        user.saveToDb()
        return {'success': 'Account successfully created'}
