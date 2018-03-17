# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class ForceArgument(ArgumentInstance):
    args = ['-f', '--force']
    kwargs = {
        'action': 'store_true',
        'dest': 'force',
        'help': 'Force the operation to complete'
    }
