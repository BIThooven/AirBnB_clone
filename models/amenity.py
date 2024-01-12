#!/usr/bin/python3
"""class inheriting from basemodel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class aminety"""
    name: str = ""
