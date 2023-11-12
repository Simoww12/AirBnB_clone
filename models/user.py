#!/usr/bin/python3
""" This module contains User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class class inherits from base model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
