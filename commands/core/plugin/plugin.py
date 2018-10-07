# python imports

# third-party imports

# platform imports
from platform.plugins import Plugins

# local imports

class Plugin(object):
    """
    Class dealing with the operations of adding,
    removing and listing plugins
    """

    def __init__(self, add_repo, rm_plugin, list, *args, **kwargs):
        self.plugin_to_add = add_repo
        self.plugin_to_remove = rm_plugin
        self.is_list = list

    def list_plugin(self):
        installed_commands = Plugins().get_plugin_commands()

        print('Following plugins are installed:')

        for each in installed_commands:
            print('{}: {}'.format(each.name, each.description))


    def execute(self):
        if self.is_list:
            self.list_plugin()
