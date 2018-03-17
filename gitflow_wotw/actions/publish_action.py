# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import ForceArgument, ShowCommandsArgument
from gitflow_wotw.components import Action


class PublishAction(Action):
    ACTION = 'publish'
    HELP_STRING = 'Publish a specific branch'

    def __init__(self):
        super(PublishAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['show_commands'] = ShowCommandsArgument()
        self.arguments['force'] = ForceArgument()

    def execute(self, parsed):
        print('Firing publish!')
        print(parsed)
