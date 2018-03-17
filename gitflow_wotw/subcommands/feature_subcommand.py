# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class FeatureSubcommand(BranchSubcommand):
    SUBCOMMAND = 'feature'
    HELP_STRING = 'Manages feature branches'

    def __init__(self):
        super(
            FeatureSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
