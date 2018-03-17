# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class VerboseArgument(ArgumentInstance):
    args = ['-v', '--verbose']
    kwargs = {
        'action': 'store_true',
        'dest': 'verbose',
        'help': 'More output'
    }
