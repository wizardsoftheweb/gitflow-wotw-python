# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class LocalArgument(Argument):
    ARGS = ['--local']
    KWARGS = {
        'action': 'store_const',
        'const': 'local',
        'dest': 'config_location',
        'help': "Use repository's config file"
    }

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
