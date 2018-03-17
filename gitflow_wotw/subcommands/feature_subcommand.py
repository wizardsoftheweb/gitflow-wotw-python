# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class FeatureSubcommand(BranchSubcommand):
    identifier = 'feature'
    help_string = 'Manages feature branches'
