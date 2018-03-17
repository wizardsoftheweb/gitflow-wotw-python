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
        if parsed.branch:
            branch = parsed.branch
        else:
            branch = None
        if parsed.base:
            base = parsed.base
        else:
            if branch:
                base = self.flow_branch.base_branch(branch)
            else:
                base = None
        print(
            "git diff %s %s" % (
                self.flow_branch.branch_to_commit_id(branch),
                self.flow_branch.branch_to_commit_id(base)
            )
        )
