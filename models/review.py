#!/usr/bin/python3
"""
    This module contains Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review left by a user for a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who left the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
