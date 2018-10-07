"""
Copyright (C) 2018 Vijaydeep Sharma <vijaydeep@sudofire.com>

License: https://bitbucket.org/sudofire/nvats/wiki/license.txt
"""

class Paths(object):
    """
    set paths used in the platform
    """

    #################################################################
    # Core packages are provided as a part of the software upon
    # installation and are crutial for normal working of the
    # the software.
    #################################################################
    core_packages = 'commands/core'

    #################################################################
    # Extra packages are the funcnalities added by the users for
    # custom behavior
    #################################################################
    extra_packages = 'commands/extra'
