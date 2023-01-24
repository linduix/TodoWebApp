'''
Module Name: auth

This module is for the authentication function
that the api will use
'''
from flaskapi import app
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, decode_token
from jwt.exceptions import ExpiredSignatureError


# init JWT
jwt = JWTManager()
jwt.init_app(app)
token_time = timedelta(days=1)

# Make token
def gen():
    token = create_access_token(identity='1', expires_delta=timedelta(seconds=1))
    return token

def verify(token):
    try:
        data = decode_token(token)
        return True, data['sub']
    except ExpiredSignatureError as e:
        return False, None