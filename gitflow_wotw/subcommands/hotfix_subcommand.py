# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class HotfixSubcommand(BranchSubcommand):
    identifier = 'hotfix'
    help_string = 'Manages hotfix branches'
