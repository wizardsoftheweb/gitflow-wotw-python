# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class KeepArgument(Argument):
    ARGS = ['-k', '--keep']
    KWARGS = {
        'action': 'store_const',
        'const': 'both',
        'dest': 'keep',
        'help': 'Keep local and remote branch after operation finishes'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
