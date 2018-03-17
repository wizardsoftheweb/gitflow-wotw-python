# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class SquashArgument(Argument):
    ARGS = ['-S', '--squash']
    KWARGS = {
        'action': 'store_true',
        'dest': 'squash',
        'help': 'Squash the operation during merge'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
