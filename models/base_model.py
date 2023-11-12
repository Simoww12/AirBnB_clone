#!/usr/bin/python3
"""
Module that contains and defines the BaseModel class
"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """
    Base class that other classes inherit from, attrs: id, crtd_@, updt_@
    """
    def __init__(self, *args, **kwargs):
        """ instantiate using id and time, can also add attrs using kwargs """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                        val,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        val,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    self.__class__.__name__ = val
                else:
                    setattr(self, key, val)
        else:
            pass

    def __str__(self):
        """ Returns a string representation of an object """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates attr updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary representation of an instance
        """
        a = {}
        for k, v in self.__dict__.items():
            if k != 'created_at' and k != 'updated_at':
                a[k] = v
        a['__class__'] = self.__class__.__name__
        a['created_at'] = self.created_at.isoformat()
        a['updated_at'] = self.updated_at.isoformat()
        return a
