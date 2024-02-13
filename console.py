#!/usr/bin/python3
"""
This module defines the console for HBNB
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    This is all about the functions in the HBNB command
    """

    prompt = "(hbnb) "

    myClasses = [BaseModel, User, Place, City, Review, State, Amenity]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """

        if line:
            class_name = line
            if class_name not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                for cls in self.myClasses:
                    if cls.__name__ == class_name:
                        inst = cls()
                        inst.save()
                        print(inst.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        from models.__init__ import storage

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            class_name, instance_id = args
            if class_name not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key in objects:
                    print(objects[instance_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        from models.__init__ import storage

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            class_name, instance_id = args
            objects = storage.all()
            if class_name not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key in objects:
                    del objects[instance_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        from models.__init__ import storage

        objects = storage.all()
        if line:
            class_name = line
            if class_name in [cls.__name__ for cls in self.myClasses]:
                instances = [str(obj) for key, obj in objects.items()
                             if key.split('.')[0] == class_name]
                print(instances)
            else:
                print("** class doesn't exist **")
        else:
            instances = [str(obj) for obj in objects.values()]
            print(instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        By adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        from models.__init__ import storage

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            instance_key = "{}.{}".format(args[0], args[1])
            if args[0] not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            elif instance_key not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            class_name, instance_id, attribute_name = args
            objects = storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)
            if class_name not in [cls.__name__ for cls in self.myClasses]:
                print("** class doesn't exist **")
            elif instance_key not in objects:
                print("** no instance found **")
            else:
                print("** value missing **")
        else:
            class_name, instance_id, attribute_name, attribute_value = args
            instance_key = "{}.{}".format(class_name, instance_id)
            objects = storage.all()
            obj = objects[instance_key]
            if attribute_name in ["id", "created_at", "updated_at"]:
                print("** cannot update id, created_at, or updated_at **")
            else:
                attr_type = type(getattr(obj, attribute_name))
                try:
                    casted_value = attr_type(attribute_value)
                except ValueError:
                    return
                setattr(obj, attribute_name, casted_value)
                obj.save()

    def do_EOF(self, line):
        """Handles end of the file to exit the program"""
        exit(0)

    def emptyline(self):
        """Overides the cmd emptyline"""

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
