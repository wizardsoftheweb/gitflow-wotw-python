# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.arguments.groups import UniversalArgumentGroup
from gitflow_wotw.components import Action, ComponentInstance


class ActionInstance(ComponentInstance, Action):

    def __init__(self):
        ComponentInstance.__init__(self)
        Action.__init__(
            self,
            self.identifier,
            self.help_string
        )
        self.arguments['universal'] = UniversalArgumentGroup()

    def execute(self, parsed):
        print("Firing %s!" % self.identifier)
        print(parsed)
