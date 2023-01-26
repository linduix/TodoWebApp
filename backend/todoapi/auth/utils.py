from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from . import SECRET_KEY

# returns: jwt token string
def gen_token(user_id: int) -> str:
    exp = datetime.now() + timedelta(days=1)
    data = {
        'sub' : str(user_id),
        'exp' : exp.timestamp()
    }
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token

# returns: valid, user_id
def verify_token(token: str) -> (bool, int):
    # decode token
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        now = datetime.now().timestamp()

        # check expiry
        if now > data['exp']:
            return False, None
        else:
            return True, int(data['sub'])
    
    # if err
    except Exception as e:
        print(e)
        return False, None
        