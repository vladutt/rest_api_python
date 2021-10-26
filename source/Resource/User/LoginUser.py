from flask_restful import Resource, reqparse
from source.Models.UserModel import UserModel
import re
from werkzeug.security import check_password_hash
import datetime
from flask_jwt_extended import create_access_token


class LoginUser(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', help="Email field is required", type=str, required=True)
        parser.add_argument('password', help="Password field is required", type=str, required=True)
        args = parser.parse_args(strict=True)

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, args.email):
            return {'email': 'Please check your email format.'}

        user = UserModel.getUserByEmail(args.email)
        if not user:
            return {'email': 'Can\'t find the an user for this email address ' % args.email}

        if check_password_hash(user.password, args.password):
            # return user.toJSON()
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200

        return {'fail': 'Wrong password...'}
