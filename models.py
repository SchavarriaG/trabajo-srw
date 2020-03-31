from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
from pymongo import MongoClient


class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)

users = []

def get_user (email):
    #for user in users:
    #    if user.email == email:
    #        return user
    #return None
    conexion = MongoClient('mongodb+srv://inmanueld:securepass@ps4games-8q85r.mongodb.net/test?retryWrites=true&w=majority')
    db = conexion.ps4
    if db.user.find_one({"email":str(email)}):
        x = db.user.find_one({"email":str(email)})
        return User(str(x.get('_id')),str(x.get('nombre')),str(x.get('email')),str(x.get('password')))
    return None


