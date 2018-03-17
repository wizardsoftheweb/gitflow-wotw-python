# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments.groups import BranchArgumentGroup
from gitflow_wotw.components import ActionInstance


class DeleteAction(ActionInstance):
    identifier = 'delete'
    help_string = 'Delete a specific branch'

    def __init__(self):
        DeleteAction.__init__(self)
        self.arguments['branches'] = BranchArgumentGroup()
