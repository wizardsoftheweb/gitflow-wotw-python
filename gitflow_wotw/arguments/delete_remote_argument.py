# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class DeleteRemoteArgument(Argument):
    ARGS = ['--delete-remote']
    KWARGS = {
        'action': 'store_const',
        'const': 'remote',
        'dest': 'delete',
        'help': 'Delete the remote branch after the operation finishes'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)