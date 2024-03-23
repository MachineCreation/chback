from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from uuid import uuid4
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

                                                                                # set variables for class instantiation

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

                                                                                # create class for generating user information and storing it in our DB(using SQLAlchemy)

def set_token(length):
        return secrets.token_hex(length)

def get_uuid():
    return uuid4().hex

                                                                # user signup
                                                                
class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.String(32), primary_key = True, unique = True, default = get_uuid)
    email = db.Column(db.String(345), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    user_name = db.Column(db.String(32), nullable = False, unique = True)
    APIkey = db.Column(db.String(255), nullable = True, default = '')
    red = db.Column(db.String(50), nullable = True, default = 'BTC')
    blue = db.Column(db.String(50), nullable = True, default = 'LTC')
    green = db.Column(db.String(50), nullable = True, default = 'ETH')
    yellow = db.Column(db.String(50), nullable = True, default = 'XTZ')
    time_zone = db.Column(db.String(100), nullable = True, default = '')
    token =db.Column(db.String(250), nullable = True, unique = True, default = set_token(24))