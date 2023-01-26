from sqlalchemy.orm import Session
from .models import User, Task
from .schema import New_taskORM, TaskORM

def new_user(db:Session, username:str, password:str, email:str=None) -> bool:
    try:
        new_user = User(email=email, username=username, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        ok = True
    except Exception as e:
        print(e)
        ok = False, None
    finally:
        print(new_user.id)
        return ok, new_user.id

def user_exists(db:Session, username:str) -> bool:
    query = db.query(User).filter_by(username=username).first()
    return query is not None
    

def get_user(id:int=None, email:str=None, username:str=None) -> User:
    if not id and not emai and not username:
        return None
    if id:
        user = User.query.filter_by(id=id).first()
        return user

# return: ok, List[TaskORM]
def get_user_tasks(db:Session, user_id:int):
    try:
        user = db.query(User).filter_by(id=user_id).first()
        tasks = user.tasks
        return True, [TaskORM.from_orm(task) for task in tasks]
    except Exception as e:
        print(e)
        return False, None


def new_task(db:Session, data:New_taskORM, id:int) -> bool:
    task = Task(**dict(data), completed=False, user_id=id)
    task.title = task.title.strip()
    try:
        db.add(task)
        db.commit()
        db.refresh(task)
        ok = True
    except Exception as e:
        print(e)
        ok = False
    return ok