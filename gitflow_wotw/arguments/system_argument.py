# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class SystemArgument(Argument):
    ARGS = ['--system']
    KWARGS = {
        'action': 'store_const',
        'const': 'system',
        'dest': 'config_location',
        'help': 'Use the system config file'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
