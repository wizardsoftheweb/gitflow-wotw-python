# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class DeleteLocalArgument(ArgumentInstance):
    args = ['--delete-local']
    kwargs = {
        'action': 'store_const',
        'const': 'local',
        'dest': 'delete',
        'help': 'Delete the local branch after the operation finishes'
    }
