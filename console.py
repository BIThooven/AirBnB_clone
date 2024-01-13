#!/usr/bin/python3
""" the console module"""
import cmd
from shlex import split
from models.base_model import BaseModel
import models


"""please to whom is gonna be debugging this code
read it carefully and go back to the tasks so you can have a grasp
of what i'm trying to implement here , because i myself got lost few times
in my own code , thank you
"""


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
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
        return SystemExit

    def EOF(self, arg) -> bool:
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self) -> bool:
        """ Do nothing when an empty line is entered """
        pass

    def create(self, line):
        """creating an instance of BaseModel"""
        if len(line) == 0:
            print('** class name missing **')
        elif line not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[line]()
            obj.save()
            print(obj.id)

    def show(self, arg):
        "string representation (class name and id)"
        _class_obj = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif _class_obj[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(_class_obj) == 1:
            print("** instance id missing **")
            return
        else:
            key = _class_obj[0] + '.' + _class_obj[1]
            instances = models.storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            else:
                obj = instances[key]
                print(str(obj))

    def destroy(self, arg):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file)"""
        target = arg.split(" ")
        if len(arg) == 0:
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

    def all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects"""
        _list = []
        _dict = models.storage.all()
        try:
            if len(arg) != 0:
                eval(arg)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        arg.strip()
        for key, val in _dict.items():
            if len(arg) != 0:
                if type(val) is eval(arg):
                    val = str(_dict[key])
                    _list.append(val)
            else:
                val = str(_dict[key])
                _list.append(val)
        print(_list)

    def update(self, line):
        """Updates an instance base on its id eg
        $ update Model id field value
        Throws errors for missing arguments"""
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
            all_instances =models.storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                models.storage.save()

    def count(self, arg):
        """getting the number of instances of a class"""
        counted = arg.split(" ")
        instance = 0
        for _obj in models.storage.all().values():
            if counted[0] == type(_obj).__name__:
                instance += 1
        print(instance)


if __name__ == "__main__":
    """infinite loop"""
    HBNBCommand().cmdloop()
