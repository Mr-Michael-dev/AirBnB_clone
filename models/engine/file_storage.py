import json

class FileStorage:
    """
    This class is responsible for serializing instances to a JSON file and deserializing JSON files back into instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        object_serialised = {}
        for key, value in self.__objects.items():
            object_serialised[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(object_serialised, file)
