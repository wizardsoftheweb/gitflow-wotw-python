# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class FetchArgument(Argument):
    ARGS = ['--file']
    KWARGS = {
        'nargs': '1',
        'dest': 'config_file',
        'metavar': 'file',
        'help': 'Use the given config file'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
