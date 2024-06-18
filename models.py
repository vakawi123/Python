from ext import db, login_manager
from flask_login import UserMixin

class Product(db.Model) :

    __tablename__= "products"

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    country = db.Column(db.String())

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    birthday = db.Column(db.Date())


class Delivery(db.Model, UserMixin):

    __tablename__ = "delivery"

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String)
    phone_number = db.Column(db.Integer())
    country = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String())
    post_code = db.Column(db.Integer)
    birthday = db.Column(db.Date())



@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(user_id)