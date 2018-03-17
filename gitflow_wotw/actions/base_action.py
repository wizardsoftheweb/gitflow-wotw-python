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
    help_string = 'Set base config'

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
        print('Firing base!')
        self.parse_config_location(parsed)

    @staticmethod
    def parse_config_location(parsed):
        print(parsed)
