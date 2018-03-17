# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class SetArgument(ArgumentInstance):
    args = ['--set']
    kwargs = {
        'nargs': 1,
        'dest': 'set',
        'metavar': 'BASE_BRANCH',
        'help': 'Use the provided branch as the base'
    }
