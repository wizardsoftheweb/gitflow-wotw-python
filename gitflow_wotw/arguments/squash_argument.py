# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class SquashArgument(ArgumentInstance):
    args = ['-S', '--squash']
    kwargs = {
        'action': 'store_true',
        'dest': 'squash',
        'help': 'Squash the operation during merge'
    }
