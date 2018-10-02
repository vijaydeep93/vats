"""
filesystem utils
"""

# python imports

# third-party imports

# platform imports

# local imports
from .path import FSPath

def get_core_packages():
    path = 'commands/core'

    return FSPath(path).get_packages()
