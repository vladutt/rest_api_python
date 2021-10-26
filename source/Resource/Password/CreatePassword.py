from flask_restful import Resource, reqparse
from source.Models.PasswordModel import PasswordModel
import re
from flask_jwt_extended import jwt_required


class CreatePassword(Resource):

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', help="Title field is required", type=str, required=True)
        parser.add_argument('login', help="Login field is required", type=str, required=True)
        parser.add_argument('password', help="Password field is required", type=str, required=True)
        parser.add_argument('website', help="Website field is required", type=str, required=True)
        args = parser.parse_args(strict=True)

        password = PasswordModel(args.title, args.login, args.password, args.website)
        password.saveToDb()
        return {'success': 'New password was successfully saved.'}
