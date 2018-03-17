# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class MessageArgument(ArgumentInstance):
    args = ['-m', '--message']
    kwargs = {
        'nargs': 1,
        'dest': 'message',
        'metavar': 'MESSAGE',
        'help': 'Use the provided message'
    }
