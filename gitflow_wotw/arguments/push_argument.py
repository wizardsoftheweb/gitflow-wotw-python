# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushArgument(ArgumentInstance):
    args = ['-p', '--push']
    kwargs = {
        'action': 'store_const',
        'const': ['all'],
        'dest': 'push',
        'help': 'Push to origin after operation completes'
    }
