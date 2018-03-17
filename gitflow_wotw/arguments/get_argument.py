# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class GetArgument(Argument):
    ARGS = ['--get']
    KWARGS = {
        'action': 'store_true',
        'dest': 'get',
        'help': 'Get the base branch'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
