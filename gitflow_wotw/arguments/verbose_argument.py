# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class VerboseArgument(Argument):
    ARGS = ['-v', '--verbose']
    KWARGS = {
        'action': 'store_true',
        'dest': 'verbose',
        'help': 'More output'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
