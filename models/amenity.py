#!/usr/bin/python3
"""
    This module contains Amenity class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class representing an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
