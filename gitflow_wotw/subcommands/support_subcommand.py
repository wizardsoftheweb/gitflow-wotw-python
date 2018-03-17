# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class SupportSubcommand(BranchSubcommand):
    SUBCOMMAND = 'support'
    HELP_STRING = 'Manages support branches'

    def __init__(self):
        super(
            SupportSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
