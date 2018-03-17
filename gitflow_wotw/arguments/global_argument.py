# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class GlobalArgument(Argument):
    ARGS = ['--global']
    KWARGS = {
        'action': 'store_const',
        'const': 'global',
        'dest': 'config_location',
        'help': 'Use the global config file'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
