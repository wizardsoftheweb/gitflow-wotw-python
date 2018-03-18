# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class FfArgument(ArgumentInstance):
    args = ['--ff']
    kwargs = {
        'action': 'store_true',
        'dest': 'fast_forward',
        'help': 'Fast-forward where possible'
    }
