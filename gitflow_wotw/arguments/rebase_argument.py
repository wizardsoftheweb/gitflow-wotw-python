# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class FetchArgument(Argument):
    ARGS = ['-r', '--rebase']
    KWARGS = {
        'action': 'store_true',
        'dest': 'rebase',
        'help': 'Rebase before merging'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
