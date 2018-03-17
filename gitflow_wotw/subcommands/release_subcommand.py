# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class ReleaseSubcommand(BranchSubcommand):
    SUBCOMMAND = 'release'
    HELP_STRING = 'Manages release branches'

    def __init__(self):
        super(
            ReleaseSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
