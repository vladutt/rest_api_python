from flask_restful import Api
from source.Resource.User.CreateUser import CreateUser
from source.Resource.User.LoginUser import LoginUser
from source.Resource.Password.CreatePassword import CreatePassword


class Routes:
    def __init__(self, app):
        api = Api(app)

        api.add_resource(CreateUser, '/register', methods=["post"])
        api.add_resource(LoginUser, '/login', methods=["post"])
        api.add_resource(CreatePassword, '/create-password', methods=["post"])
