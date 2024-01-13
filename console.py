#!/usr/bin/python3
""" the console module"""
import cmd
from shlex import split
from models.base_model import BaseModel
import sys
import models


"""please to whom is gonna be debugging this code
read it carefully and go back to the tasks so you can have a grasp
of what i'm trying to implement here , because i myself got lost few times
in my own code , thank you
"""


class HBNBCommand(cmd.Cmd):
    from models.engine.file_storage import FileStorage
    """ HBNB class"""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.state import State
    from models.review import Review
    from models.user import User
    prompt = "(hbnb)"

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def quit(self, arg) -> bool:
        """Quit command to exit the program"""
        return True

    def EOF(self, arg) -> bool:
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self) -> bool:
        """ Do nothing when an empty line is entered """
        pass

    def create(self, *arg):
        """creating an instance of BaseModel"""
        if arg:
            if arg in self.classes:
                get_class = getattr(sys.modules[__name__], arg)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def show(self, arg):
        "string representation (class name and id)"
        if len(split(arg)) == 0:
            print("** class name missing **")
        elif len(split(arg)) == 1:
            print("** instance id missing **")
        elif split(arg)[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            _dic = models.storage.all()
            keys = split(arg)[0] + "." + str(split(arg)[1])
            if keys in _dic:
                print(_dic[keys])
            else:
                print("** no instance found **")
        return

    def destroy(self, arg):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file)"""
        if len(split(arg)) == 0:
            print("** class name missing **")
        elif len(split(arg)) == 1:
            print("** instance id missing **")
        elif split(arg)[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            _dict = models.storage.all()
            key = split(arg)[0] + '.' + split(arg)[1]
            if key in _dict:
                del _dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects"""
        _list = []
        _dict = models.storage.all()
        if len(split(arg)) == 0:
            for key in _dict:
                __class = str(_dict[key])
                _list.append(__class)
            print(_list)
            return
        if split(arg) not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            __class = ""
            for key in _dict:
                classesname = key.split('.')
                if classesname[0] == split(arg)[0]:
                    __class = str(_dict[key])
                    _list.append(__class)
            print(_list)

    def update(self, arg):
        """Updates an instance base on its id eg
        $ update Model id field value
        Throws errors for missing arguments"""
        if len(split(arg)) == 0:
            print("** class name missing **")
            return
        elif len(split(arg)) == 1:
            print("** instance id missing **")
            return
        elif len(split(arg)) == 2:
            print("** attribute name missing **")
            return
        elif len(split(arg)) == 3:
            print("** value missing **")
            return
        elif split(arg)[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keys = split(arg)[0] + "." + split(arg)[1]
        _dict = models.storage.all()
        try:
            instance = _dict[keys]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeO = type(getattr(instance, split(arg)[2]))
            split(arg)[3] = typeO(split(arg)[3])
        except AttributeError:
            pass
        setattr(instance, split(arg)[2], split(arg)[3])
        models.storage.save()

    def count(self, arg):
        """getting the number of instances of a class"""
        instance_num = 0
        dic = models.storage.all()
        if split(arg)[0] not in self.classes:
            print("** class doen't exist **")
            return
        else:
            for key in dic:
                _class = key.split()
                if _class[0] == split(arg)[0]:
                    instance_num += 1
            print(instance_num)


if __name__ == "__main__":
    """infinite loop"""
    HBNBCommand().cmdloop()
