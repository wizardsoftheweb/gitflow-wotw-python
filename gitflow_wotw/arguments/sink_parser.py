# pylint: disable=W,C,R

from gitflow_wotw.constants import HIERARCHY
from gitflow_wotw.util import ObservesHierarchy


class SinkParser(ObservesHierarchy):

    def __init__(self, identifier=None, help_string=None, tier=None):
        if tier is None:
            tier = HIERARCHY[2]
        super(SinkParser, self).__init__(tier)
        self.identifier = identifier
        self.help_string = help_string
        self.parser = None

    def add_parser(self, subparsers=None):
        self.parser = subparsers.add_parser(
            self.identifier,
            description=self.help_string,
            help=self.help_string
        )

    def attach(self, subparsers=None):
        self.add_parser(subparsers)

    def print_help(self):
        self.parser.print_help()
