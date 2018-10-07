# python imports

# third-party imports

# platform imports
from platform.plugins import BaseCommand

# local imports

class Command(BaseCommand):
    """
    Class to hook plugin to platform
    """

    name = 'plugin'

    add = (
        ('--add',),
        {'dest': 'add_repo', 'help': 'Add a repo as a plugin. Requires a git link'}
    )

    remove = (
        ('--rm',),
        {'dest': 'rm_plugin', 'help': 'Removes a plugin. Requires a plugin name'}
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

    def execute(self, *args, **kwargs):
        print(kwargs)
