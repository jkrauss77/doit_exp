def task_echo():
    """Echo arguments"""
    return {
        'actions': ['echo %(arg)s'],
        'verbosity': 2,
        'params':[{'name':'arg',
                       'short':'a',
                       'long': 'arg',
                       'type': str,
                       'default':'default value',
                       'help': 'helpful message about this flag'}]
        }