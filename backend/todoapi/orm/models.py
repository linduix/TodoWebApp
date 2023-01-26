from sqlalchemy import (
        Boolean, String, Integer, 
        Column, ForeignKey, Text, Date
    )    
from sqlalchemy.orm import relationship
from . import Base, engine

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)  # int - Primary key 🔑
    title = Column(String(50), nullable=False)  # str
    description = Column(Text, nullable=True)  # str
    due_date = Column(Date, nullable=True)  # date object
    completed = Column(Boolean, nullable=False)  # bool
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=False
    )  # int - Foreign key 🗝️

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)  # int - Primary key 🔑
    email = Column(String(50), unique=True)  # str
    username = Column(String(20), unique=True, nullable=False)  # str
    password = Column(String(), nullable=False)  # str (ha2shed)
    tasks = relationship("Task", backref="user", lazy=True)

Base.metadata.create_all(bind=engine)