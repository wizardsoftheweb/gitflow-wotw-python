# pylint:disable=W,C,R

from gitflow_wotw.arguments import SinkParser


class Action(SinkParser):

    def execute(self, parsed):
        """A specific task to be defined by instances"""
