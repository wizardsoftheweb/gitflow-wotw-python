# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Subcommand


class SubcommandInstance(Subcommand):
    SUBCOMMAND = ''
    HELP_STRING = ''
    ACTIONS = []

    def __init__(self):
        super(
            SubcommandInstance,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
        self.populate()

    def populate(self):
        for action in self.ACTIONS:
            self[action.identifier] = action
