# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class HotfixSubcommand(BranchSubcommand):
    SUBCOMMAND = 'hotfix'
    HELP_STRING = 'Manages hotfix branches'

    def __init__(self):
        super(
            HotfixSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
