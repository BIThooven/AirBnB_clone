#!/usr/bin/python3
"""class User that inherits from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
