# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class FfArgument(Argument):
    ARGS = ['--ff']
    KWARGS = {
        'action': 'store_true',
        'dest': 'fast_forward',
        'help': 'Fast-forward where possible'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
