"""
filesystem module dealing with paths
"""

# python imports
from pathlib import Path
from abc import ABC, abstractmethod

# third-party imports

# platform imports

# local imports

class BaseFSPath(ABC):
    """
    Base class dealing filesystem paths.

    This class uses pathlib for all path manupulations
    To read more on pathlib go through the Documantation here.
    Documantation: https://docs.python.org/3/library/pathlib.html
    """

    path = None

    def __init__(self, path):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path(path)

    def get_sub_dirs(self):
        """
        returns a list of dirs in a given path
        """

        return [sub_path for sub_path in self.path.iterdir() if sub_path.is_dir()]


class FSPath(BaseFSPath):
    """
    Class dealing with the spacifice requirement
    """

    def __init__(self, path):
        super().__init__(path)

    def get_packages(self):
        """
        Returns all the packages in folder
        """
        return [str(sub_path.name) for sub_path in self.path.iterdir() if sub_path.is_dir()]

    def get_modules(self):
        """
        Returns all the modules in a folder
        """

        return [str(sub_path.name) for sub_path in self.path.iterdir() if sub_path.is_suffix == '.py']
