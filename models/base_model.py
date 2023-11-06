#!/usr/bin/env python3
""" This models contians one class,
BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    "A parent class that all the upcoming classes will inherit form"

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        "Updates the public instance attribute updated_at with"
        "the current datetime"
        self.updated_at = datetime.now()

    def to_dict(self):
        "Returns a dictionary representation of the class"
        dict_objct = self.__dict__.copy()
        dict_objct['__class__'] = self.__class__.__name__
        dict_objct['created_at'] = self.created_at.isoformat()
        dict_objct['updated_at'] = self.updated_at.isoformat()
        return dict_objct
    
        
    def __str__(self):
        "should print: [<class name>] (<self.id>) <self.__dict__>"
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.to_dict())
