from ..db import db
from sqlalchemy import func


class PasswordModel(db.Model):
    __tablename__ = 'passwords'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(126))
    login = db.Column(db.String(126))
    password = db.Column(db.String(255))
    website = db.Column(db.String(126))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, title, login, password, website):
        self.title = title
        self.login = login
        self.password = password
        self.website = website

    def toJSON(self):
        return {'title': self.title, 'login': self.login, 'password': self.password, 'website': self.website}

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

