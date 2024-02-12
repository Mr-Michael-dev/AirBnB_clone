#!/usr/bin/python3
"""
This modue defines a City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel

    Attributes:
        state_id: string -it will be the state.id
        name: string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation method"""

        super().__init__(*args, **kwargs)
