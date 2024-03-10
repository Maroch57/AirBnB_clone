#!/usr/bin/python3
"""
This module defines the User class.

The User class represents a user in the system and
inherits from the BaseModel class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
