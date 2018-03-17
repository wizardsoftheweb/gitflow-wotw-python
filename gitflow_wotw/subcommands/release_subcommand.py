# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import BranchSubcommand


class ReleaseSubcommand(BranchSubcommand):
    identifier = 'release'
    help_string = 'Manages release branches'
