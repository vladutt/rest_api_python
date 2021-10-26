from flask import Flask
from .routes import Routes
import sys
# LOGIN MANGER IMPORT TODO
from .db import db
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"


    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://testing:1234567890@159.69.87.162:3306/testing"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
    jwt = JWTManager(app)
    db.init_app(app)

    Routes(app)

    create_database(app)

    return app


def create_database(app):
    if 'create_database' in sys.argv:
        from .Models import UserModel, PasswordModel

        db.create_all(app=app)
        print('database was create')