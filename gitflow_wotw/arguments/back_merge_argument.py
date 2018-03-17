# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class BackMergeArgument(Argument):
    ARGS = ['-b', '--back-merge']
    KWARGS = {
        'action': 'store_true',
        'dest': 'back_merge',
        'help': 'Back merge where possible'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
