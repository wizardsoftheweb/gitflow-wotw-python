# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class HelpArgument(ArgumentInstance):
    args = ['-h', '--help']
    kwargs = {
        'action': 'help',
        'dest': 'help',
        'help': 'Print this help message and exit'
    }
