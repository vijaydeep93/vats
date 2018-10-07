"""
Copyright (C) 2018 Vijaydeep Sharma <vijaydeep@sudofire.com>

License: https://bitbucket.org/sudofire/nvats/wiki/license.txt
"""

# python imports
import subprocess

# third-party imports

# platform imports
from platform.plugins import Plugins
from platform.filesystem import Paths, filesystem

# local imports

class Plugin(object):
    """
    Class dealing with the operations of adding,
    removing and listing plugins
    """

    def __init__(self, repo, plugin, list, *args, **kwargs):
        self.plugin_to_add = repo
        self.plugin_to_remove = plugin
        self.is_list = list

    def list_plugin(self):
        installed_commands = Plugins().get_plugin_commands()

        print('Following plugins are installed:')

        for each in installed_commands:
            print('{}: {}'.format(each.name, each.description))


    def add_plugin(self):
        extra_dir_path = filesystem.FileSystem(Paths.extra_packages)
        extra_sub_dirs = set(extra_dir_path.get_sub_dirs()) # existing dir

        git_call = ['git', '-C', str(extra_dir_path), 'clone', self.plugin_to_add] # git clone
        subprocess.call(git_call)

        new_sub_dirs = set(extra_dir_path.get_sub_dirs()) - extra_sub_dirs # newly added dir

        for dir in map(filesystem.FileSystem, new_sub_dirs):
            dir_name = dir.name

            dir.join_path('.git')
            dir.rm_dir()

            print('Success! Added plugin dir {}'.format(dir_name))

    def rm_plugin(self):
        dir = filesystem.FileSystem(Paths.extra_packages)
        dir.join_path(self.plugin_to_remove)
        dir.rm_dir()

        print('Success! Removed plugin {}'.format(dir.name))

    def execute(self):
        if self.is_list:
            self.list_plugin()

        if self.plugin_to_add:
            self.add_plugin()

        if self.plugin_to_remove:
            self.rm_plugin()
