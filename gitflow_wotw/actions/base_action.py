# pylint:disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.arguments import (
    BaseArgument,
    BranchArgument,
    GetArgument,
    SetArgument
)
from gitflow_wotw.components import ActionInstance, ArgumentGroup


class BaseAction(ActionInstance):
    identifier = 'base'
    help_string = 'Set base branch'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['branch'] = BranchArgument()
        self.arguments['base'] = BaseArgument()
        seed = OrderedDict()
        seed['get'] = GetArgument()
        seed['set'] = SetArgument()
        self.arguments['mutators'] = ArgumentGroup(
            seed=seed,
            exclusive=True
        )

    def execute(self, parsed):
        if not parsed.branch:
            if parsed.set:
                return self.set_base(None, parsed.set)
            return self.get_base()
        else:
            if not parsed.base:
                if parsed.set:
                    return self.set_base(parsed.branch, parsed.set)
            else:
                if parsed.set:
                    if parsed.set == parsed.base:
                        return self.set_base(parsed.branch, parsed.set)
                    else:
                        raise ValueError(
                            '--set and base are different;'
                            ' remove one and try again'
                        )
                else:
                    return self.set_base(parsed.branch, parsed.base)
            return self.get_base(parsed.branch)

    def get_base(self, branch=None):
        self.flow_branch.base_branch(branch)

    def set_base(self, branch=None, base=None):
        self.flow_branch.update_base(branch, base)
