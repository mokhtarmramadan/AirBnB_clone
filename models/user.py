#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represents a User.

    Attributes:
        email (str): email of the user.
        password (str): password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """
=======
    "Represents a User"
>>>>>>> 4189381413ffb2171ffcbb9fbec7a3af7606f71f

    email = ""
    password = ""
    first_name = ""
    last_name = ""
