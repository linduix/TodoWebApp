from pydantic import BaseModel


class TokenData(BaseModel):
    sub: int


SECRET_KEY = "test"
