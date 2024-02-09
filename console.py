#!/usr/bin/python3
"""This module defines the  console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """This is all about the functions in the HBNB command"""

    prompt = "(hbnb)"


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