# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import BaseArgument, BranchArgument
from gitflow_wotw.components import ActionInstance


class DiffAction(ActionInstance):
    identifier = 'diff'
    help_string = 'Compare the branch against its base'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['branch'] = BranchArgument()
        self.arguments['base'] = BaseArgument()

    def execute(self, parsed):
        print(parsed)
        print(self.flow_branch.branch_to_commit_id())
        print(self.flow_branch.branch_to_commit_id(
            self.flow_branch.base_branch()
        ))
