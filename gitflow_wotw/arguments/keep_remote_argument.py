# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class KeepRemoteArgument(Argument):
    ARGS = ['--keep-remote']
    KWARGS = {
        'action': 'store_const',
        'const': 'remote',
        'dest': 'keep',
        'help': 'Keep the remote branch after the operation completes'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
