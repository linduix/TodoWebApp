'''
Module Name: main.py

This is the main script for the flask backend server
'''

from flask import Flask, request
from flask_restful import Api, Resource


class Hello(Resource):
    '''Api Hello endpoint'''

    def get(self):
        '''get method'''
        name = request.args.get('name')
        print(name)
        return {"hello": name if name else "world"}

    def post(self):
        body = request.json


app = Flask(__name__)
api = Api(app)
api.add_resource(Hello, '/hello')


@app.route('/hi', methods=['GET'])
def hi_endpoint():
    '''server endpoint methood'''
    return "hello"


if __name__=='__main__':
    app.run()
