#!/usr/bin/python3
"""Defines the MyConsole console."""
import cmd
import re
from shlex import split
from mymodels import storage
from mymodels.mymodel import MyBaseModel
from mymodels.mymodel_user import MyUser
from mymodels.mymodel_state import MyState
from mymodels.mymodel_city import MyCity
from mymodels.mymodel_place import MyPlace
from mymodels.mymodel_amenity import MyAmenity
from mymodels.mymodel_review import MyReview

def parse(input_string):
    "Parsing input"
    curly_braces = re.search(r"\{(.*?)\}", input_string)
    brackets = re.search(r"\[(.*?)\]", input_string)
    if curly_braces is None:
        if brackets is None:
            return [item.strip(",") for item in split(input_string)]
        else:
            lexer = split(input_string[:brackets.span()[0]])
            ret_list = [item.strip(",") for item in lexer]
            ret_list.append(brackets.group())
            return ret_list
    else:
        lexer = split(input_string[:curly_braces.span()[0]])
        ret_list = [item.strip(",") for item in lexer]
        ret_list.append(curly_braces.group())
        return ret_list

class MyConsole(cmd.Cmd):
    """Defines the MyConsole command"""

    prompt = "(myconsole) "
    __myclasses = {
        "MyBaseModel",
        "MyUser",
        "MyState",
        "MyCity",
        "MyPlace",
        "MyAmenity",
        "MyReview"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, input_string):
        """Default behavior for cmd module when input is invalid"""
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", input_string)
        if match is not None:
            input_list = [input_string[:match.span()[0]], input_string[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", input_list[1])
            if match is not None:
                command = [input_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_dict.keys():
                    call = "{} {}".format(input_list[0], command[1])
                    return command_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(input_string))
        return False

    def do_quit(self, input_string):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, input_string):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, input_string):
        """Usage: create"""
        input_list = parse(input_string)
        if len(input_list) == 0:
            print("** class name missing **")
        elif input_list[0] not in MyConsole.__myclasses:
            print("** class doesn't exist **")
        else:
            print(eval(input_list[0])().id)
            storage.save()

    def do_show(self, input_string):
        """Usage"""
        input_list = parse(input_string)
        obj_dict = storage.all()
        if len(input_list) == 0:
            print("** class name missing **")
        elif input_list[0] not in MyConsole.__myclasses:
            print("** class doesn't exist **")
        elif len(input_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input_list[0], input_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(input_list[0], input_list[1])])

    def do_destroy(self, input_string):
        """Usage: destroy """
        input_list = parse(input_string)
        obj_dict = storage.all()
        if len(input_list) == 0:
            print("** class name missing **")
        elif input_list[0] not in MyConsole.__myclasses:
            print("** class doesn't exist **")
        elif len(input_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input_list[0], input_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(input_list[0], input_list[1])]
            storage.save()

    def do_all(self, input_string):
        """Usage: all or all <class> or <class>.all()"""
        input_list = parse(input_string)
        if len(input_list) > 0 and input_list[0] not in MyConsole.__myclasses:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(input_list) > 0 and input_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(input_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, input_string):
        """Usage: count <class> or <class>.count()"""
        input_list = parse(input_string)
        count = 0
        for obj in storage.all().values():
            if input_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, input_string):
        """Usage: update <class> <id> <attribute_name> <attribute>"""
        input_list = parse(input_string)
        obj_dict = storage.all()

        if len(input_list) == 0:
            print("** class name missing **")
            return False
        if input_list[0] not in MyConsole.__myclasses:
            print("** class doesn't exist **")
            return False
        if len(input_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(input_list[0], input_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(input_list

