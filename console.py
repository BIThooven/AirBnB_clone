#!/usr/bin/python3
"""
The console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """Contains functionality of the console"""
    prompt = "(hbnb) "
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def do_create(self, arg):
        """Creates a new object"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        """
        cls_obj = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif cls_obj[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(cls_obj) == 1:
            print("** instance id missing **")
            return
        else:
            key = cls_obj[0] + "." + cls_obj[1]
            instances = models.storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            else:
                obj = instances[key]
                print(str(obj))

    def do_update(self, line):
        """Updates attributes of an object"""
        updates = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif updates[0] not in __class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(updates) == 1:
            print("** instance id missing **")
            return
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + updates[1]
            instances = models.storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            else:
                obj = instances[key]
                setattr(obj, updates[2], updates[3])
                models.storage.save()

    def do_destroy(self, args):
        """Destroys an object based on the Class Name and ID"""

        target = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif target[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(target) == 1:
            print("** instance id missing **")
            return
        else:
            key = target[0] + "." + target[1]
            instances = models.storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            else:
                del instances[key]
                models.storage.save()

    def do_all(self, line):
        """Print string representation of all instances"""
        _list = []
        objs = models.storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, value in objs.items():
            if len(line) != 0:
                if type(value) is eval(line):
                    value = str(objs[key])
                    _list.append(value)
            else:
                value = str(objs[key])
                _list.append(value)
        print(_list)

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        return True

    def do_quit(self, args):
        """Quits the interpreter"""
        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
