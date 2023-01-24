from flaskapi import app, db, session
from flaskapi.models import *
from sys import argv, exit

with app.app_context():
    try:
        if argv[1] == 'destroy':
            print('Destruction!!')
            db.drop_all()
            exit(0)
    except IndexError:
        print('ID USERNAME EMAIL PASSWORD')
        for user in User.query.all():
            print(user.id, user.username, user.email, user.password)
        print('----------')
        for task in Task.query.all():
            print(task.__dict__)