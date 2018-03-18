# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import BranchArgument
from gitflow_wotw.components import ActionInstance


class CheckoutAction(ActionInstance):
    identifier = 'checkout'
    help_string = 'Check out a specific branch'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['branch'] = BranchArgument(False)

    def execute(self, parsed):
        self.checkout_branch(parsed.branch)

    def checkout_branch(self, branch=None):
        self.flow.branch.change_branch(branch)
