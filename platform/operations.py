"""
Copyright (C) 2018 Vijaydeep Sharma <vijaydeep@sudofire.com>

License: https://bitbucket.org/sudofire/nvats/wiki/license.txt

File handling platform operations
"""

# python imports

# third-party imports

# platform imports
from platform.io.input import Prompt

# local imports

class Operation(object):
    """
    Entry class of the program
    """

    def get_prompt(self):
        """
        Returns the command and args
        """

        args = Prompt().parse()
        command = args.command
        del args.command
        return command, vars(args)

    def execute(self):
        """
        Execute command
        """

        command, kwargs = self.get_prompt()
        command.hook(**kwargs)
