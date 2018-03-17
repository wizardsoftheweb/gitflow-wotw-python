# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class PushTagArgument(Argument):
    ARGS = ['--push-tag']
    KWARGS = {
        'action': 'append_const',
        'const': 'tag',
        'dest': 'push',
        'help': 'Push tag after operation finishes'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
