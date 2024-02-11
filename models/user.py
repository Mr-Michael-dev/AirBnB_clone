#!/usr/bin/python3
"""
This module defines the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel

    Attributes:
        email: string
        password: string
        first_name: string
        last_name: string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Instantiation method"""

        super().__init__()
