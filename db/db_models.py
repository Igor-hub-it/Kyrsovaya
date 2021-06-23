from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


USER_LENGTH = 15
PERS_DATA_LENGTH = 31

db = SQLAlchemy(app)


class Dates(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    date = db.Column(db.TEXT(10), unique=True)


class Requests(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user = db.Column(db.TEXT(USER_LENGTH), nullable=False)
    time = db.Column(db.TEXT(5), nullable=False)
    pers_data = db.Column(db.TEXT(PERS_DATA_LENGTH))
    comment = db.Column(db.TEXT(200))
    id_dates = db.Column(db.INTEGER, nullable=False)


class User(UserMixin, db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user = db.Column(db.TEXT(USER_LENGTH), unique=True)
    pers_data = db.Column(db.TEXT(PERS_DATA_LENGTH), unique=True)
    password = db.Column(db.TEXT(1025), nullable=False)
