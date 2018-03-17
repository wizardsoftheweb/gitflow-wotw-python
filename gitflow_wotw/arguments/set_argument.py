# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class SetArgument(Argument):
    ARGS = ['--set']
    KWARGS = {
        'nargs': 1,
        'dest': 'set',
        'help': 'Use the provided branch as the base'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
