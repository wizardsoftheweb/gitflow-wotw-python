# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.arguments.groups import UniversalArgumentGroup
from gitflow_wotw.components import Action, ComponentInstance


class ActionInstance(ComponentInstance, Action):
    pre_execution = OrderedDict()
    post_execution = OrderedDict()

    def __init__(self):
        ComponentInstance.__init__(self)
        Action.__init__(
            self,
            self.identifier,
            self.help_string
        )
        self.arguments['universal'] = UniversalArgumentGroup()
        self.pre_execution['tidy_branches'] = []

    def pre_execute(self, parsed):
        for handler, args in self.pre_execution.items():
            self.handlers[handler](self, parsed, *args)

    def execute(self, parsed):
        print("Firing %s!" % self.identifier)
        print(parsed)

    def post_execute(self, parsed):
        for handler, args in self.post_execution.items():
            self.handlers[handler](self, parsed, *args)
