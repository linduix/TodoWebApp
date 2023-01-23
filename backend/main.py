"""
Module Name: main

This is the main script module for the flask backend server
"""  
from flaskapi import app, db
# from flaskapi import app, db
# from flaskapi.models import User, Task

if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        session = db.session
        for user in User.query.all():
            print(user.id, user.username, user.password)
    pass
