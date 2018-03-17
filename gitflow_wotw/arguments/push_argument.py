# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class PushArgument(Argument):
    ARGS = ['-p', '--push']
    KWARGS = {
        'action': 'store_const',
        'const': ['all'],
        'dest': 'push',
        'help': 'Push to origin after operation completes'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
