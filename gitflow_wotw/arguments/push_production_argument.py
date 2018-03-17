# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class PushProductionArgument(Argument):
    ARGS = ['--push-production']
    KWARGS = {
        'action': 'append_const',
        'const': 'production',
        'dest': 'push',
        'help': 'Push production after operation finishes'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
