# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class MessageFileArgument(Argument):
    ARGS = ['--message-file']
    KWARGS = {
        'nargs': 1,
        'dest': 'message_file',
        'metavar': 'MESSAGE_FILE',
        'help': 'Use the contents of the provided file as the tag message'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
