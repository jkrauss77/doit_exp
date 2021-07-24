# all commands must start with task_ in order to be recognized by dodo. 

import glob
from doit.action import CmdAction
from my_imports.stuff import *

# runnning doit by itself will only run specified tasks, plus any dependencies found naturally or specified. If not
# declared, doit will runn all tasks in order defined. 
DOIT_CONFIG = {'default_tasks': ['call_func']}

def task_hello_world():
    """This is an example of some docs that would be showed."""
    return {
        'actions': ['echo hello'],
        'verbosity': 2,
        }

def task_fibonacci():
    """Show the fibonacci numbers from 0 to Nth specified value"""
    return {
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

def task_format():
    return {'actions': ["python3 sample/sample.py"],
            'file_dep': glob.glob("/workspace/sample/*")}

def task_compile():
    return {'actions': ["echo compiling && clang++ -Wall -std=c++11 include/main.cpp -o build/main"],
            'file_dep': ['include/main.cpp'],
            'targets': ['build/main'],
            'verbosity': 2}


# There is a dependency on foo.txt, running the command that depends on it will run dependencies automatically 
def task_modify():
    return {'actions': ["echo bar > foo.txt"],
            'file_dep': ["foo.txt"],
            }

def task_create():
    return {'actions': ["touch foo.txt"],
            'targets': ["foo.txt"]
            }

# wildcard selection
def task_t1():
    return {'actions': ["echo task1"],
            'verbosity': 2}
def task_t2():
    return {'actions': ["echo task2"],
            'verbosity': 2}
def task_t3():
    return {'actions': ["echo task3"],
            'verbosity': 2}


def task_fail():
    return {'actions': ["exit 1"]}


# gain access to task metadata
def who(task):
    print('my name is', task.name)
    print(task.targets)

def task_x():
    return {
        'actions': [who],
        'targets': ['asdf'],
        'verbosity': 2,
        }



def show_cmd(task):
    return "executing... %s" % task.name

def task_title():
    return {'actions': ["echo task3"],
            'title': show_cmd,
            'verbosity': 2}


# Task dependency
def task_package():
    return {'actions': ['echo packaging up junk with certain version %(v)s'],
            'getargs': {'v': ('version', 'out')},
            'task_dep':['version'],
            'uptodate': [False],
            'verbosity': 2}

def task_version():
    return {'actions': [CmdAction("echo 1.0.6", save_out='out')],
            'verbosity': 2}