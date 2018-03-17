# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushTagArgument(ArgumentInstance):
    args = ['--push-tag']
    kwargs = {
        'action': 'append_const',
        'const': 'tag',
        'dest': 'push',
        'help': 'Push tag after operation finishes'
    }
