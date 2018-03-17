# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class InteractiveArgument(Argument):
    ARGS = ['-i', '--interactive']
    KWARGS = {
        'action': 'store_true',
        'dest': 'interactive',
        'help': 'Perform an interactive rebase'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
