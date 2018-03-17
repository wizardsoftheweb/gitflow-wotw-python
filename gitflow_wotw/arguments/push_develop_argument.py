# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class PushDevelopArgument(Argument):
    ARGS = ['--push-develop']
    KWARGS = {
        'action': 'append_const',
        'const': 'develop',
        'dest': 'push',
        'help': 'Push develop after operation finishes'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
