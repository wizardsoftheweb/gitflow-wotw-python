# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import VerboseArgument
from gitflow_wotw.components import Action


class ListAction(Action):
    ACTION = 'list'
    HELP_STRING = 'Lists a set of branches'

    def __init__(self):
        super(ListAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['verbose'] = VerboseArgument()

    def execute(self, parsed):
        print('Firing list!')
        print(parsed)
