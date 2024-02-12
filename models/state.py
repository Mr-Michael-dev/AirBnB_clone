#!/usr/bin/python3
"""
This module defines the state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel

    Attributes:
        name: string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation method"""

        super().__init__(*args, **kwargs)
