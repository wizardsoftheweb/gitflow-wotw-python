# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import BranchArgument
from gitflow_wotw.arguments.groups import BranchArgumentGroup
from gitflow_wotw.components import ActionInstance


class DeleteAction(ActionInstance):
    identifier = 'delete'
    help_string = 'Delete a specific branch'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['branch'] = BranchArgument()
        self.arguments['branches'] = BranchArgumentGroup()
        self.post_execution['delete_branch'] = []
