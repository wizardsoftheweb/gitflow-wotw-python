# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ArgumentInstance


class MessageFileArgument(ArgumentInstance):
    args = ['--message-file']
    kwargs = {
        'nargs': 1,
        'dest': 'message_file',
        'metavar': 'MESSAGE_FILE',
        'help': 'Use the contents of the provided file as the tag message'
    }
