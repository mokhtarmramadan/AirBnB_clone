#!/usr/bin/python3
"""This model supplies one class,
FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    "Represent an abstracted storage engine"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(FileStorage.__file_path) as f:
                dict_objct = json.load(f)
                for v in dict_objct.values():
                    class_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            return
