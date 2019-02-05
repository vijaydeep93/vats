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
    Entry class of the program.

    Binds the command line promt with command plugin.
    """

    def get_prompt(self):
        """
        Returns the command and args
        """

        # capture the CLI promt input
        args = Prompt().parse()

        # get the top-level command
        command = args.command
        del args.command

        # return the command and its args as dict
        return command, vars(args)

    def execute(self):
        """
        Execute command
        """

        command, kwargs = self.get_prompt()

        # excute the command with given parameter
        command.hook(**kwargs)
