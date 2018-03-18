# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class BugfixSubcommand(BranchSubcommand):
    identifier = 'bugfix'
    help_string = 'Manages bugfix branches'
