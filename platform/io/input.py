"""
This module deal with all the inputs for the platform.
"""

# python imports
import argparse, sys
from abc import ABC, abstractmethod

# third-party imports

# platform imports

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

        default_arguments = []

        return default_arguments + self.arguments

    def add_arguments(self, parser, arguments=[]):
        """
        Adds given arguments in the given parser
        """

        for argument in arguments:
            parser.add_argument(**argument)

        return parser

    def get_loaded_parser(self):
        """
        Returns a parser loaded with arguments
        """
        return self.add_arguments(self.get_parser(), arguments=self._get_arguments())

    def get_namespace(self):
        return Namespace()

    def add_sub_parser(self, parser, *args, **kwargs):
        return parser.add_subparsers(*args, **kwargs)

    def add_command(self, subparser, *args, **kwargs):
        return subparser.add_parser(*args, **kwargs)

    @abstractmethod
    def parse(self):
        pass


class Prompt(BasePrompt):
    """
    Reads and parses the input given on the command line prompt
    """

    def parse(self, streem=sys.argv, namespace=None):
        if not namespace:
            namespace = self.get_namespace()

        parser = self.get_loaded_parser()
        return parser.parse_args(streem, namespace=namespace)
