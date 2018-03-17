# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class RenameAction(ActionInstance):
    identifier = 'rename'
    help_string = 'Renames a specific branch'
