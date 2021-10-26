from ..db import db
from sqlalchemy import func
from werkzeug.security import generate_password_hash
import datetime


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(126), unique=True, index=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(255))
    is_active = db.Column(db.Integer, default=1)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    passwords = db.relationship('PasswordModel', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def toJSON(self):
        return {'id': self.id, 'email': self.email, 'username': self.username}

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkUserIfExists(cls, email):
        user = cls.getUserByEmail(email)
        return not (user is None)

    @classmethod
    def getUserByEmail(cls, email):
        return cls.query.filter_by(email=email).first()


