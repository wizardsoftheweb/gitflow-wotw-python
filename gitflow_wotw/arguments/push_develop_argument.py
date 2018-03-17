# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushDevelopArgument(ArgumentInstance):
    args = ['--push-develop']
    kwargs = {
        'action': 'append_const',
        'const': 'develop',
        'dest': 'push',
        'help': 'Push develop after operation finishes'
    }
