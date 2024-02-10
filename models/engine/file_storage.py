#!/usr/bin/python3
"""
Thie module contains FileStorage class
"""
import json


class FileStorage:
    """
    This class is responsible for serializing instances to a JSON fil
    and deserializing JSON files back into instances.
    """

    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        from models.base_model import BaseModel


        def serialize(obj):
            if isinstance(obj, BaseModel):
                return obj.to_dict()
            return obj

        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file, default=serialize)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing
        """
        import os

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
