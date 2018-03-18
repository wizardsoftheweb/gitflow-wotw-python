# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class GetArgument(ArgumentInstance):
    args = ['--get']
    kwargs = {
        'action': 'store_true',
        'default': True,
        'dest': 'get',
        'default': True,
        'help': 'Get the base branch',
        'opt_out': True
    }
