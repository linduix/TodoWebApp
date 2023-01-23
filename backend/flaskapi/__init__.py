'''
Module Name: __init__

Init module for flask api
'''
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flaskapi.endpoints import *

# init app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# init api
api = Api(app)
api.add_resource(task, "/hello")

# init db
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

from flaskapi.models import User, Task