from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Intrest(db.Model):
    __tablename__='intrests'

    id = db.Column(db.Integer,primary_key = True)
    intrest_name = db.Column(db.String)
    description = db.Column(db.String)
    

class UserIntrests(db.Model):

    __tablename__ ='user_intrests'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer("user.id"))
    intrest_id = db.Column(db.Integer,db.ForeignKey("intrest.id"))
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Comment('{self.comment}', '{self.posted}')"
