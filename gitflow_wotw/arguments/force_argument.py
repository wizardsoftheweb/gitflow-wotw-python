# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class ForceArgument(Argument):
    ARGS = ['-f', '--force']
    KWARGS = {
        'action': 'store_true',
        'dest': 'force',
        'help': 'Force the operation to complete'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
