# python imports

# third-party imports

# platform imports
from platform.plugins import BaseCommand

# local imports
from .plugin import Plugin

class Command(BaseCommand):
    """
    Class to hook plugin to platform
    """

    name = 'plugin'
    description = "Plugin to add, remove, list other plugins"

    add = (
        ('--add',),
        {'dest': 'repo', 'help': 'Add a repo as a plugin. Requires a git link'}
    )

    remove = (
        ('--rm',),
        {'dest': 'plugin', 'help': 'Removes a plugin. Requires a plugin name'}
    )

    list = (
        ('--list',),
        {'action': 'store_true', 'help': 'Lists all the extra install plugin'}
    )

    def get_arguments(self):
        return [
            self.add,
            self.remove,
            self.list
        ]

    def hook(self, *args, **kwargs):
        Plugin(**kwargs).execute()
