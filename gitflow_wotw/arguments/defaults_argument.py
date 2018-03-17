# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class DefaultsArgument(Argument):
    ARGS = ['-D', '--defaults']
    KWARGS = {
        'action': 'store_true',
        'dest': 'defaults',
        'help': 'Use defaults where possible'
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
