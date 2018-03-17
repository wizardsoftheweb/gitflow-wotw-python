# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class BugfixSubcommand(BranchSubcommand):
    SUBCOMMAND = 'bugfix'
    HELP_STRING = 'Manages bugfix branches'

    def __init__(self):
        super(
            BugfixSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
