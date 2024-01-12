#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances"""
import json


class FileStorage():
    """serializing instances to json file and deserializing json files"""
    from models.base_model import BaseModel
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.state import State
    from models.review import Review
    from models.user import User
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returning dict objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects with key <obj class name>.id"""
        key = obj.self.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                for key, value in json.load(f).items():
                    attribute = eval(value['__class__'])(**value)
                    self.__objects[key] = attribute
        except FileNotFoundError:
            pass
