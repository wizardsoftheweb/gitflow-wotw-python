# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class HelpArgument(Argument):
    ARGS = ['-h', '--help']
    KWARGS = {
        'action': 'help',
        'dest': 'help',
        'help': 'Print this help message and exit'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
