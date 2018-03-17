# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class SupportSubcommand(BranchSubcommand):
    identifier = 'support'
    help_string = 'Manages support branches'
