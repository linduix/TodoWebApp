"""
Module Name: endpoints

This module contains the endpoints that 
will be used by the flask api

Endpoints Included: /task, 
"""
from flask import request, jsonify, make_response
from flask_restful import Resource
from flaskapi.models import new_user, get_user


class Task(Resource):
    """
    This endpoint will handle all requests
    relating to tasks eg. creation, deletion, etc.
    """


class Signup(Resource):
    """
    This endpoint is for signup requests
    to create new users in the db
    """

    def post(self):
        username = request.form['username']
        password = request.form['password']

        # check required
        if not username:
            return "Username required", 400
        if not password:
            return "Password token required", 400

        # create user and catch errors
        try:
            new_user(username, password)
            response = make_response("Success!", 201)
        except Exception as e:
            print(f"ERROR: {e}")
            response = make_response({"Error": f"{e}"}, 500)
        finally:
            return response


class Validate(Resource):
    """
    This endpoint will be used to validate
    the user's email adress
    """

    def get(self):
        id = request.args.get("id")
        auth = request.args.get("auth")
        if not id:
            return "Id required", 400
        if not auth:
            return "Auth token required", 400

        response.headers["Content-Type"] = "application/json"
        return response
