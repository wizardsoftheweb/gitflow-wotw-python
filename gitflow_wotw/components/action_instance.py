# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.components import Action


class ActionInstance(Action):
    ACTION = ''
    HELP_STRING = ''
    ARGUMENTS = []

    def __init__(self):
        super(ActionInstance, self).__init__(
            self.ACTION,
            self.HELP_STRING
        )
        self.populate()

    def populate(self):
        for argument in self.ARGUMENTS:
            self.arguments[argument.identifier] = argument

    def execute(self, parsed):
        print("Firing %s!" % self.ACTION)
        print(parsed)
