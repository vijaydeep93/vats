"""
filesystem utils
"""

# python imports

# third-party imports

# platform imports

# local imports
from .filesystem import FileSystem
from . import Paths

def get_core_packages():
    path = Paths.core_packages

    return FileSystem(path).get_packages()

def get_extra_packages():
    path = Paths.extra_packages

    return FileSystem(path).get_packages()
