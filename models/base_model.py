#!/ur/bin/python3
"""model base"""
import uuid as u
import datetime as d
import models


class BaseModel():
    """class base """
    def __init__(self, *args, **kwargs):
        """constructors for the class base"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    crt = d.datetime.fromisoformat(value)
                    self.created_at = crt
                elif key == 'updated_at':
                    upd = d.datetime.fromisoformat(value)
                    self.updated_at = upd
                else:
                    setattr(self, key, value)
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
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    """__str__ method to return string representation"""
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def __repr__(self):
        """returns the str representation"""
        return (self.__str__())
