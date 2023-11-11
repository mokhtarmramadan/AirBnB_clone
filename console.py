#!/usr/bin/env python3
"""This model supplies one class,
HBNBCommand entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    "Class that implements the console prompt"
    prompt = "(hbnb) "

    def do_EOF(self, line):
        "Exit the program when EOF is written"
        return True
    
    def do_quit(self, line):
        "Exit the program when quit is written"
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
