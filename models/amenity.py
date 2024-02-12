#!/usr/bin/python3
"""
This module defines the amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel

    Attributes:
        name: string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation method"""

        super().__init__(*args, **kwargs)
