from flask import Flask, request
from flask_restful import Api, Resource, reqparse


class Hello(Resource):
    def get(self):
        name = request.args.get('name')
        print(name)
        return {"hello": name if name else "world"}

    def post(self):
        pass


app = Flask(__name__)
api = Api(app)
api.add_resource(Hello, '/hello')


@app.route('/hi', methods=['GET'])
def hi():
    return "hello"


if __name__=='__main__':
    app.run()