# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import ShowCommandsArgument
from gitflow_wotw.components import Action


class CheckoutAction(Action):
    ACTION = 'checkout'
    HELP_STRING = 'Check out a specific branch'

    def __init__(self):
        super(CheckoutAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing checkout!')
        print(parsed)
