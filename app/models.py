from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class LiveScore():

    def __init__(self, league_name, home_name, away_name, score, time, status):
    
        self.league_name = league_name
        self.home_name = home_name
        self.away_name = away_name
        self.score = score
        self.time = time
        self.status = status

class Fixture():

    def __init__(self, h_name, a_name, date, time, location):
    
        self.h_name = h_name
        self.a_name = a_name
        self.date = date
        self.time = time
        self.location = location

    
class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index =True)
    phone_number = db.Column(db.Integer, unique = True, index = True) 
    password_hash = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    
    UserInterests = db.relationship('UserInterest', backref = 'user', lazy = 'dynamic')
 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
 
class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(255), index = True)
    UserInterests = db.relationship('UserInterest', backref = 'interests', lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.title}'

    def save_Interest(cls):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_interests(cls):
        interests = Interest.query,all()
        return interests


class UserInterest(db.Model):

    __tablename__ = "userinterests"

    id = db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"))
