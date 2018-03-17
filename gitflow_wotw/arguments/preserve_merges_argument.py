# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class PreserveMergesArgument(Argument):
    ARGS = ['-P', '--preserve-merges']
    KWARGS = {
        'action': 'store_true',
        'dest': 'preserve_merges',
        'help': 'Preserve merges while rebasing'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
