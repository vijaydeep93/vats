"""
Copyright (C) 2018 Vijaydeep Sharma <vijaydeep@sudofire.com>

License: https://bitbucket.org/sudofire/nvats/wiki/license.txt

This module deal with all the inputs for the platform.
"""

# python imports
import argparse
from abc import ABC, abstractmethod

# third-party imports

# platform imports
from platform.plugins import Plugins

# local imports

class Namespace(argparse.Namespace):
    """
    Namespace class user to store the parsed data.

    Will set the default properties
    """

    pass


class BasePrompt(ABC):
    """
    Base class providing an interface with the cli prompt.

    This class impliments the argparse package of python.
    To read more on argparse go through the Documantation here.
    Documantation: https://docs.python.org/3/library/argparse.html
    """

    parser = None
    namespace = None
    arguments = []

    def get_parser(self):
        """
        returns an argument parser object
        """

        if self.parser:
            return self.parser

        parser_description = "Welcome to nvats. It rocks!"
        return argparse.ArgumentParser(description=parser_description)

    def _get_arguments(self):
        """
        returns a list of tuples of arguments that needs be parsed.
        to add more arguments in child classes just override the arguments property.
        """

        ######################################################
        # should have following format
        # [((posinal agrs), {keyword arguments dict}),
        # ((posinal agrs), {keyword arguments dict})]
        ######################################################
        default_arguments = []

        return default_arguments + self.arguments

    def add_arguments(self, parser, arguments=[]):
        """
        Adds given arguments in the given parser
        """

        for args, kwargs in arguments:
            parser.add_argument(*args, **kwargs)

        return parser

    def get_loaded_parser(self):
        """
        Returns a parser loaded with arguments
        """
        return self.add_arguments(self.get_parser(), arguments=self._get_arguments())

    def get_namespace(self):
        return Namespace()

    def add_subparser(self, parser, *args, **kwargs):
        """
        Adds subparser for commands
        """

        return parser.add_subparsers(*args, **kwargs)

    def add_command(self, subparser, *args, **kwargs):
        """
        Adds a command to given subparser.

        A command is sub-module or a package that can be added to
        enhance the funcnality of the platform.
        """

        return subparser.add_parser(*args, **kwargs)

    def set_defaults(self, subparser, *args, **kwargs):
        """
        Add defaults for a parser
        """

        subparser.set_defaults(*args, **kwargs)
        return subparser

    @abstractmethod
    def parse(self):
        pass


class Prompt(BasePrompt):
    """
    Reads and parses the input given on the command line prompt
    """

    def add_commands(self, subparser, commands):
        """
        Adds the commands(packages/plugins) to given parsers of given type
        """

        for command in commands:
            command_parser = self.add_command(subparser, command.name, help=command.description)
            command_parser = self.add_arguments(command_parser, command.get_arguments())
            command_parser = self.set_defaults(command_parser, command=command)

        return subparser

    def parse(self):
        """
        Returns a Namespace object after loading all the
        commands(packages/plugins) and parsing the sys.agrv
        """

        plugins = Plugins().get_plugin_commands()

        namespace = self.get_namespace()
        parser = self.get_loaded_parser()
        subparser = self.add_subparser(parser, dest='name', required=True)
        subparser = self.add_commands(subparser, commands=plugins)

        return parser.parse_args(namespace=namespace)
