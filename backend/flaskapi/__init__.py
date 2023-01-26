"""
Module Name: __init__

Init module for flask api
"""
from flask import Flask, session
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# init app
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = "test"

# init db
db = SQLAlchemy(app)
session = db.session
from flaskapi.models import User, Task

with app.app_context():
    db.create_all()

# init api
api = Api(app)
from flaskapi.endpoints import *

api.add_resource(Signup, "/signup")
api.add_resource(Validate, "/validate")
