from typing import List
from datetime import date
from pydantic import BaseModel

class New_taskORM(BaseModel):
    title : str
    description : str = None
    due_date : date = None

class TaskORM(New_taskORM):
    completed : bool
    user_id : int
    class Config:
        orm_mode = True

class User_tasks(BaseModel):
    tasks: List[TaskORM]
    class Config:
        orm_mode = True