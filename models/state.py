s module contains State class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The State class represents a state and inherits from the BaseModel class.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
