# pylint:disable=W,C,R

from gitflow_wotw.arguments.groups import UniversalArgumentGroup
from gitflow_wotw.parsers import ParserSink


class Action(ParserSink):

    def __init__(self, *args, **kwargs):
        ParserSink.__init__(self, *args, **kwargs)
        self.arguments['universal'] = UniversalArgumentGroup()

    def execute(self, parsed):
        """A specific task to be defined by instances"""
