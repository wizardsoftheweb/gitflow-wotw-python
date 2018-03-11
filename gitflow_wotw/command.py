# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import SourceParser
from gitflow_wotw.util import HasDescendants


class Command(SourceParser, HasDescendants):
    IDENTIFIER = 'wotw'
    HELP_STRING = 'An ambitious attempt to duplicate gitflow-avh in Python'

    def __init__(self):
        OrderedDict.__init__(self)
        SourceParser.__init__(
            self,
            'wotw',
            'An ambitious attempt to duplicate gitflow-avh in Python'
        )
        HasDescendants.__init__(self, self.below)

    def attach_below(self):
        for _, descendant in self.items():
            descendant.attach(self.subparsers)

    def print_help_below(self):
        for _, descendant in self.items():
            descendant.print_help()

    def bootstrap(self, args=None):
        self.attach()
        known, unknown = self.parse_args(args)
        self.execute(known)
