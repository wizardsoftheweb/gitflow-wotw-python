# pylint:disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import Parser
from gitflow_wotw.util import HasDescendants


class Subcommand(Parser, HasDescendants, OrderedDict):

    def __init__(self, identifier=None, help_string=None):
        OrderedDict.__init__(self)
        Parser.__init__(self, identifier, help_string)
        HasDescendants.__init__(self, self.below)

    def attach_below(self):
        for _, descendant in self.items():
            descendant.attach(self.subparsers)

    def print_help_below(self):
        for _, descendant in self.items():
            descendant.print_help()
