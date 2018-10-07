"""
This module deal with all the inputs for the platform.
"""

# python imports
import argparse
from abc import ABC, abstractmethod
from importlib import import_module

# third-party imports

# platform imports
from commands import Command
from platform.filesystem.utils import (
    get_core_packages,
    get_extra_packages
)

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

    @abstractmethod
    def parse(self):
        pass


class Prompt(BasePrompt):
    """
    Reads and parses the input given on the command line prompt
    """

    def get_packages(self, type):
        """
        Returns all the packages of the given type
        """

        if type == Command.core:
            return get_core_packages()

        return get_extra_packages()

    def collect_arguments(self, type):
        """
        Returns the collected arguments from the given type of packages
        """

        args = {}

        for package in self.get_packages(type):
            try:
                # import a module from a package
                module = import_module('commands.{}.{}'.format(type, package))

                # add to args
                args[module.name] = module.arguments
            except Exception as e:
                print("The package '{}' seems to be corrupt. Error: '{}'".format(package, e))

        return args

    def add_commands(self, subparser, type):
        """
        Adds the commands(packages/plugins) to given parsers of given type
        """

        for command, arguments in self.collect_arguments(type).items():
            command_parser = self.add_command(subparser, command)
            command_parser = self.add_arguments(command_parser, arguments)

        return subparser

    def parse(self, namespace=None):
        """
        Returns a Namespace object after loading all the
        commands(packages/plugins) and parsing the sys.agrv


        """

        if not namespace:
            namespace = self.get_namespace()

        parser = self.get_loaded_parser()

        subparser = self.add_subparser(parser, dest='command', required=True)

        subparser = self.add_commands(subparser, type=Command.core)
        subparser = self.add_commands(subparser, type=Command.extra)

        return parser.parse_args(namespace=namespace)
