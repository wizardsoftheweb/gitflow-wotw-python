# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class BackMergeArgument(ArgumentInstance):
    args = ['-b', '--back-merge']
    kwargs = {
        'action': 'store_true',
        'dest': 'back_merge',
        'help': 'Back merge where possible'
    }
