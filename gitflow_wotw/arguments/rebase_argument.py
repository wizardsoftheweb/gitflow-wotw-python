# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class RebaseArgument(ArgumentInstance):
    args = ['-r', '--rebase']
    kwargs = {
        'action': 'store_true',
        'dest': 'rebase',
        'help': 'Rebase before merging'
    }
