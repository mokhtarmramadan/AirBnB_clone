#!/usr/bin/env python3
""" This models contians one class,
BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    "A parent class that all the upcoming classes will inherit form"

    def __init__(self, *args, **kwargs):
        "Initiate a attributes"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v

    def save(self):
        "Updates the public instance attribute updated_at with"
        "the current datetime"
        self.updated_at = datetime.now()

    def to_dict(self):
        "Returns a dictionary representation of the class"
        dict_objct = self.__dict__.copy()
        dict_objct['id'] = self.id
        dict_objct['created_at'] = str(self.created_at)
        dict_objct['updated_at'] = str(self.updated_at)
        dict_objct['__class__'] = self.__class__.__name__
        return (dict_objct)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
