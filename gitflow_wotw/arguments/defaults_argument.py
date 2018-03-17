# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class DefaultsArgument(ArgumentInstance):
    args = ['-D', '--defaults']
    kwargs = {
        'action': 'store_true',
        'dest': 'defaults',
        'help': 'Use defaults where possible'
    }
