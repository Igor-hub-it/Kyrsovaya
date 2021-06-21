from app import app
from flask_sqlalchemy import SQLAlchemy


USER_LENGTH = 15

db = SQLAlchemy(app)


class Dates(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    date = db.Column(db.String(10), unique=True)


class Requests(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user = db.Column(db.String(USER_LENGTH), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    pers_data = db.Column(db.String(30))
    comment = db.Column(db.String(200))
    id_dates = db.Column(db.INTEGER, nullable=False)
