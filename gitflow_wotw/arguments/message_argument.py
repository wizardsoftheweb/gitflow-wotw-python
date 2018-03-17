# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class MessageArgument(Argument):
    ARGS = ['-m', '--message']
    KWARGS = {
        'nargs': 1,
        'dest': 'message',
        'help': 'Use the provided message'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
