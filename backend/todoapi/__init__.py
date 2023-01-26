'''
Init module for my api-pkg
'''

from fastapi import FastAPI
app = FastAPI()

from .endpoints import *