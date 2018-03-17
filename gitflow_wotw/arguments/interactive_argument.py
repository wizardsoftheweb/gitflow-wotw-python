# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class InteractiveArgument(ArgumentInstance):
    args = ['-i', '--interactive']
    kwargs = {
        'action': 'store_true',
        'dest': 'interactive',
        'help': 'Perform an interactive rebase'
    }
