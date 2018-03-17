# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class SignArgument(Argument):
    ARGS = ['-s', '--sign']
    KWARGS = {
        'action': 'store_true',
        'dest': 'sign',
        'help': 'Sign the operation'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
