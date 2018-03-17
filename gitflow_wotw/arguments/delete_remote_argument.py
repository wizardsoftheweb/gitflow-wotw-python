# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class DeleteRemoteArgument(ArgumentInstance):
    args = ['--delete-remote']
    kwargs = {
        'action': 'store_const',
        'const': 'remote',
        'dest': 'delete',
        'help': 'Delete the remote branch after the operation finishes'
    }
