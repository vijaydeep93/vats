"""
Copyright (C) 2018 Vijaydeep Sharma <vijaydeep@sudofire.com>

License: https://bitbucket.org/sudofire/nvats/wiki/license.txt

File handling plugins
"""

# python imports
from abc import ABC, abstractmethod
from importlib import import_module

# third-party imports

# platform imports
from commands import CommandType
from deck.filesystem.utils import (
    get_core_packages,
    get_extra_packages
)

# local imports


class BaseCommand(ABC):
    """
    Class to be inherited in all the commands
    """

    name = None
    description = None

    def __str__(self):
        return self.name

    @abstractmethod
    def get_arguments(self):
        """
        Returns all the arguments for a commands
        """
        pass

    @abstractmethod
    def hook(self, *agrs, **kwargs):
        """
        hooks the command and its argument with a funtion to excute.
        """
        pass


class Plugins(object):
    """
    Class handling all the plugin package

    This class imports the commands from core plugin as well as
    extra plugins.
    """

    def get_packages(self, type):
        """
        Returns all the packages of the given type
        """

        if type == CommandType.core:
            return get_core_packages()

        return get_extra_packages()

    def import_command(self, type, package):
        """
        Imports command class from packages and returns it's object
        """

        try:
            # import a module from a package and return command object
            return import_module('commands.{}.{}'.format(type, package)).Command()

        except Exception as e:
            print("The package '{}' seems to be corrupt. Error: '{}'".format(package, e))

    def get_plugin_commands(self):
        """
        Returns all the command available across all the core and extra plugins
        """

        commands = []

        # add core commands
        for package in self.get_packages(CommandType.core):
            command = self.import_command(CommandType.core, package)
            commands.append(command)

        # add extra commands
        for package in self.get_packages(CommandType.extra):
            command = self.import_command(CommandType.extra, package)
            commands.append(command)

        # TODO: get rid of the if condition here
        return [command for command in commands if command]
