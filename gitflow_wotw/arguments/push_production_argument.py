# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class PushProductionArgument(ArgumentInstance):
    args = ['--push-production']
    kwargs = {
        'action': 'append_const',
        'const': 'production',
        'dest': 'push',
        'help': 'Push production after operation finishes'
    }
