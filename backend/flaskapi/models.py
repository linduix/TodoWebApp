'''
Module Name: models

This module contains the db models 
and db methoods that flask api will use

Tables Included: Task, User
Methoods Included: new_user, get_user
'''
from datetime import date
from flaskapi import db, session


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # int - Primary key 🔑
    title = db.Column(db.String(50), nullable=False) # str
    description = db.Column(db.Text) # str
    due_date = db.Column(db.Date) # date object
    completed = db.Column(db.Boolean, nullable=False) # bool
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # UUID - Foreign key 🗝️

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # UUID - Primary key 🔑
    email = db.Column(db.String(50), unique=True, nullable=False) # str
    username = db.Column(db.String(20), unique=True, nullable=False) # str
    password = db.Column(db.String(), nullable=False) # str (ha2shed)
    tasks = db.relationship('Task', backref='user', lazy=True) # Task entry relationship


def new_user(username, password, email='none'):
    new_user = User(email=email, username=username, password=password)
    session.add(new_user)
    session.commit()

def get_user(id=None, email=None, username=None):
    if not id and not emai and not username:
        return None
    if id:
        user = User.query.filter_by(id=id).first()
        return user