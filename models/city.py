#!/usr/bin/python3
"""class City inherting from basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    state_id: str = ""
    name: str = ""
