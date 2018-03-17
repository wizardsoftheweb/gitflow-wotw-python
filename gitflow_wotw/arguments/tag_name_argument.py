# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Argument


class TagNameArgument(Argument):
    ARGS = ['-T', '--tag-name']
    KWARGS = {
        'action': 'store_true',
        'dest': 'tag_name',
        'help': 'Use the provided tag name'
    }
    NEGATABLE = False

    def __init__(self):
        Argument.__init__(self, *self.ARGS, **self.KWARGS)
