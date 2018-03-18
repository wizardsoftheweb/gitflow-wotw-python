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
        print(
            "git diff %s %s" % (
                self.flow.remote.hash_from_branch(parsed.branch),
                self.flow.remote.hash_from_branch(parsed.base)
            )
        )
