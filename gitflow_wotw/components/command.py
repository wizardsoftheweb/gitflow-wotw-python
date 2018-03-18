# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.parsers import ParserSource
from gitflow_wotw.constants import HIERARCHY
from gitflow_wotw.components import Subcommand


class Command(ParserSource, Subcommand):

    def __init__(self, identifier=None, help_string=None):
        Subcommand.__init__(
            self,
            identifier,
            help_string,
            HIERARCHY[0]
        )
        ParserSource.__init__(
            self,
            identifier,
            help_string,
            HIERARCHY[0]
        )

    def bootstrap(self, args=None):
        self.attach()
        known, unknown = self.parse_args(args)
        self.execute(known)
