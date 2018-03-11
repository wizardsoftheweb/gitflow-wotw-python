# pylint: disable=W,C,R

from gitflow_wotw.constants import HIERARCHY
from gitflow_wotw.arguments import SinkParser


class Parser(SinkParser):

    def __init__(self, identifier=None, help_string=None, tier=None):
        if tier is None:
            tier = HIERARCHY[1]
        super(Parser, self).__init__(identifier, help_string, tier)
        self.subparsers = None

    def add_subparsers(self):
        self.subparsers = self.parser.add_subparsers(
            dest=self.below,
            help="Available %ss" % self.below
        )

    def attach_below(self):
        """Attach descendant parsers"""

    def attach(self, subparsers=None):
        self.add_parser(subparsers)
        self.add_subparsers()
        self.attach_below()

    def print_help_below(self):
        """Calls print_help on everything below"""

    def print_help(self):
        self.parser.print_help()
        self.print_help_below()
