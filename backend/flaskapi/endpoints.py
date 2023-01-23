'''
Module Name: endpoints

This module contains the endpoints that 
will be used by the flask api

Endpoints Included: /task, 
'''
from flask import request
from flask_restful import Resource


class task(Resource):
    """
    This will be the task endpoint that will handle all interactions
    that relate to the todo-tasks themselves
    """


