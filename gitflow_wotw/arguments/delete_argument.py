# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class DeleteArgument(ArgumentInstance):
    args = ['-d', '--delete']
    kwargs = {
        'action': 'store_const',
        'const': 'both',
        'dest': 'delete',
        'help': 'Delete local and remote branch after operation finishes'
    }
