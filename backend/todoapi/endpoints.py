from . import app
from .auth import utils
from .orm import SessionLocal, crud, schema
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, exceptions, Depends, Form, Header

# for syntax checking
def has_whitespace(string) -> bool:
    for letter in string.strip():
        if letter.isspace():
            return True
    return False


# to generate db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# returns: unauthorised_exception (if validation fails), user_id
def validate_session(authorization: str) -> (exceptions.HTTPException, int):
    # setup
    unauthorized_exception = HTTPException(401, "Unauthorized/invalid token")

    # check if token given
    if not authorization:
        return unauthorized_exception, None
    authorization = authorization.strip()

    # check if bearer and validate token
    bearer, token = authorization.split(" ")
    if bearer.lower() == "bearer":
        valid, user_id = utils.verify_token(token)
        if not valid:
            return unauthorized_exception, None

    return None, user_id


# ------------------- Endpoints -----------------------

class User_form_login(BaseModel):
    username: str
    password: str

class User_form_signup(User_form_login):
    email: str = None

class Token_json(BaseModel):
    token: str

# --- /user ---
# sign up
@app.post("/user", status_code=201, response_model=Token_json)
async def sign_up(form: User_form_signup, db: Session = Depends(get_db)):

    # Setup
    username = form.username.strip()
    password = form.password.strip()
    if form.email:
        email = form.email.strip()
    whitespace_exception = HTTPException(
        400, detail="Username and password can't contain whitespace"
    )
    user_exists_excetption = HTTPException(409, detail="Username already exists")
    db_error_exception = HTTPException(
        500, detail="Something went wrong when creating user"
    )

    # Syntax check for username and password
    if has_whitespace(password) or has_whitespace(username):
        raise whitespace_exception

    # Check if username in database
    if crud.user_exists(db, username):
        raise user_exists_excetption

    # Add user to db
    ok, user_id = crud.new_user(db, username, password)
    if not ok:
        raise db_error_exception

    # Gen token
    token:str = utils.gen_token(user_id)

    return Token_json(token=token)

# log in
@app.get('/user', status_code=200, response_model=Token_json)
async def log_in(form: User_form_login, db: Session = Depends(get_db)):
    
    # Setup
    username = form.username.strip()
    password = form.password.strip()
    username_404_exception = HTTPException(
        404, detail="User not found"
    )
    username_password_exception = HTTPException(
        400, detail="Username or password invalid"
    )
    db_error_exception = HTTPException(
        500, detail="Something went wrong when creating user"
    )

    # Syntax check for username and password
    if has_whitespace(password) or has_whitespace(username):
        raise username_password_exception

    # Get user
    user = crud.get_user(db, username=username)

    # Check if username exsiste
    if not username:
        raise username_404_exception

    # Gen token
    token:str = utils.gen_token(user.id)

    return Token_json(token=token)

# get user's tasks
@app.get("/user/tasks", status_code=200, response_model=schema.User_tasks)
async def get_user_tasks(
    db: Session = Depends(get_db), authorization: str = Header(None)
):
    # setup
    db_error_exception = HTTPException(
        500, detail="Something went wrong when creating user"
    )

    # validate user
    unauthorised_exception, user_id = validate_session(authorization)
    if unauthorised_exception:
        raise unauthorised_exception

    # get task list
    ok, tasks = crud.get_user_tasks(db, user_id)
    if ok:
        return schema.User_tasks(tasks=tasks)
    else:
        raise db_error_exception


# --- /task ---
# add task
@app.post("/task", status_code=201)
async def create_task(
    task: schema.New_taskORM,
    db: Session = Depends(get_db),
    authorization: str = Header(None),
):

    # validate the user and get user_id
    unauthorised_exception, user_id = validate_session(authorization)

    # if unauthorized raise exception
    if unauthorised_exception:
        raise unauthorised_exception

    # create task
    ok = crud.new_task(db, task, user_id)

    if ok:
        return None
    else:
        raise HTTPException(500, "Something went wrong when creating task")

# delete task
@app.delete('/task', status_code=204)
def delete_task():
    pass

# /test
@app.get("/test", status_code=200)
async def test(authorization: str = Header(None)) -> int:
    # validate session
    unauthorised_exception, user_id = validate_session(authorization)

    # if unauthorized raise exception
    if unauthorised_exception:
        raise unauthorised_exception

    return user_id
