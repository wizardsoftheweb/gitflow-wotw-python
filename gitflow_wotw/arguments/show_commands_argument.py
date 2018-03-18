# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class ShowCommandsArgument(ArgumentInstance):
    args = ['--show-commands']
    kwargs = {
        'action': 'store_true',
        'dest': 'show_commands',
        'help': 'Display git commands as they are used'
    }
