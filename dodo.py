# all commands must start with task_ in order to be recognized by dodo. 

def task_hello_world():
    """This is an example of some docs that would be showed."""
    return {
        'actions': ['echo hello'],
        'verbosity': 2,
        }

def task_fibonacci():
    """Show the fibonacci numbers from 0 to Nth specified value"""
    return {
        'params':[    {'name':'param2',
                       'type': int,
                       'default':0,
                        'help': 'This is the number of fibonacci numbers you would like to see.'}],
        'actions': ['python3 fibonacci.py 7'],
        'verbosity': 2,
    }

def func_with_args(arg_first, arg_second):
    print(arg_first)
    print(arg_second)
    return True

def task_call_func():
    return {
        'actions': [(func_with_args, [], {
            'arg_second': 'This is a second argument.',
            'arg_first': 'This is a first argument.'})
        ],
        'verbosity': 2,
    }

def task_python_version():
    return {
        'actions': [['python', '--version']],
        'doc': 'Gives the current python version'
        }

def task_count():
    for i in range(3):
        yield { 'name': i,
                'actions': ["echo %i" % i],
                'verbosity': 2}