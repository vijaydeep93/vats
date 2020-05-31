"""
Copyright (C) 2018 Vijaydeep Sharma <vdsharma93@gmail.com>

License: https://github.com/vijaydeep93/vats/wiki/license.txt

filesystem utils
"""

# python imports

# third-party imports

# platform imports

# local imports
from .filesystem import FileSystem
from . import Paths

def get_core_packages():
    """
    Returns a list of packages of core commands
    """

    path = Paths.core_packages

    return FileSystem(path).get_packages()

def get_extra_packages():
    """
    Returns a list of packages of extra commands added
    """

    path = Paths.extra_packages

    return FileSystem(path).get_packages()
