#!/usr/bin/python3
""" This module contains City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from base model """
    state_id = ""
    name = ""
