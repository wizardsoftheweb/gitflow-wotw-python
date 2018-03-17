# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class TagArgument(Argument):
    ARGS = ['-t', '--tag']
    KWARGS = {
        'action': 'store_true',
        'dest': 'tag',
        'help': 'Tag the repo after the operation finishes'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
