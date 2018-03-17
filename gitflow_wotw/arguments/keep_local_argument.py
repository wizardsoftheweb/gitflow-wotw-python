# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class KeepLocalArgument(Argument):
    ARGS = ['--keep-local']
    KWARGS = {
        'action': 'store_const',
        'const': 'both',
        'dest': 'local',
        'help': 'Keep the local branch after the operation finishes'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
