#!/usr/bin/python3
"""
This module represents a BaseModel class.
it defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for other classes.

    Attributes:
        id: a string autogenerated by uuid module
        created_at: time in which the instance is created
        updated_at: updates with current time everytime the object changes

    Methods:
        __init__(): instantiates a class
        __str__(): prints the string representation of the class instance
        save(): updates the public instance attribute 'updated_at'
        to_dict(): returns a dictionary containing\
        all the keys/values of the instance
    """

    def __init__(self):
        """
        class instantiation method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        prints the string representation of the instance
        """
        my_str = f"[BaseModel] ({self.id} self.__dict__)"

        return my_str
    
    def save(self):
        """
        updates 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        Returns the dictionary representation of the BaseModel
        """