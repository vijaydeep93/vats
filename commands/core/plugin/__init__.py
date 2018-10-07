name = 'plugin'
arguments = []

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

arguments.append(add)
arguments.append(remove)
arguments.append(list)
