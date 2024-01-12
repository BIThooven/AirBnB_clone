#!/ur/bin/python3
"""model base"""
import uuid as u
import datetime as d
import models


class BaseModel():
    """class base """
    def __init__(self, *args, **kwargs):
        """constructors for the class base"""

        if kwargs:
            """setting each key as attribute name
            and each value in this dictionary
            """
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            """converting strings into datetime objects
            checking if key == created_at and if value == updated_at
            """
            if key == "created_at":
                value = d.datetime.strptime(value,
                                            '%Y-%m-%dT%H:%M:%S.%f')
            if key == "updated_at":
                value = d.datetime.strptime(value,
                                            '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(u.uuid4())
            self.created_at = d.datetime.now()
            self.updated_at = d.datetime.now()
            models.storage.new(self)

    """public instance attribute to update updated_at"""
    def save(self):
        self.updated_at = d.datetime.now()
        models.storage.save()

    """public instance for __dict__ representation"""
    def to_dict(self):
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

    """__str__ method to return string representation"""
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
