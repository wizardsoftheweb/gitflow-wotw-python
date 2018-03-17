# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Command


class CommandInstance(Command):
    COMMAND = ''
    HELP_STRING = ''
    SUBCOMMANDS = []

    def __init__(self):
        super(
            CommandInstance,
            self
        ).__init__(
            self.COMMAND,
            self.HELP_STRING
        )
        self.populate()

    def populate(self):
        for subcommand in self.SUBCOMMANDS:
            self[subcommand.identifier] = subcommand
