from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(102))


# class Request(db.Model):
#     __tablename__ = "request"
#
#     index = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     response_time = db.Column(db.Float)
#     date = db.Column(db.DateTime)
#     method = db.Column(db.String(128))
#     size = db.Column(db.Integer)
#     status_code = db.Column(db.Integer)
#     path = db.Column(db.String(128))
#     user_agent = db.Column(db.String(128))
#     remote_address = db.Column(db.String(128))
#     exception = db.Column(db.String(128))
#     referrer = db.Column(db.String(128))
#     browser = db.Column(db.String(128))
#     platform = db.Column(db.String(128))
#     mimetype = db.Column(db.String(128))
