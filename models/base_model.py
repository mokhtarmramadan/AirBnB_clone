#!/usr/bin/python3
"""Defines the BaseModel class."""""" This models contians one class,
BaseModel that defines all common attributes/methods for other classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A parent class that all the upcoming classes will inherit form"""

    def __init__(self, *args, **kwargs):
        """Initialize the object"""
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        "Updates the public instance attribute updated_at with"
        "the current datetime"
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        "Returns a dictionary representation of the class"
        dict_objct = self.__dict__.copy()
        dict_objct["created_at"] = self.created_at.isoformat()
        dict_objct["updated_at"] = self.updated_at.isoformat()
        dict_objct["__class__"] = self.__class__.__name__
        return dict_objct

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
