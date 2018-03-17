# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class DeleteLocalArgument(Argument):
    ARGS = ['--delete-local']
    KWARGS = {
        'action': 'store_const',
        'const': 'local',
        'dest': 'delete',
        'help': 'Delete the local branch after the operation finishes'
    }
    NEGATABLE = True

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
