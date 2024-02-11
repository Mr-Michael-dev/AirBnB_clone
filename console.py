#!/usr/bin/python3
"""This module defines the  console"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is all about the functions in the HBNB command"""

    prompt = "(hbnb) "


    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """

        if line:
            if line == "BaseModel":
                base = BaseModel()
                base.save()
                print(base.id)
            else:
                print("** class doesn't exist **")
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
            print("** instance id missing **")
        elif len(args) == 2:
            class_name, instance_id = args
            objects = storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key in objects:
                print(objects[instance_key])
            else:
                print("** no instance found **")





        # objects = storage.all()
        # instance_key = ("{}.{}".format(class_name, instance_id))
        # if instance_key in storage.all():
        #     print(objects[instance_key])
        # else:
        #     print("** no instance found **")




            # arg1, arg2 = args
            # if arg1 != str(__class__.__name__):
            #     print("** class doesn't exist ***")
            # else:
            #     instance = f"{arg1}.{arg2}"
            #     for key, value in storage.all().items():
            #         if key in instance:
            #             print(value)
            #         else:
            #             print("** no instance found **")

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
