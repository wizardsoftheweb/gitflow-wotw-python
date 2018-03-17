# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class FfMasterArgument(Argument):
    ARGS = ['--ff-master']
    KWARGS = {
        'action': 'store_true',
        'dest': 'ff_master',
        'help': 'Fast-forward master'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
