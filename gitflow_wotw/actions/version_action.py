# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action


class VersionAction(Action):
    ACTION = 'version'
    HELP_STRING = 'List program version'

    def __init__(self):
        super(VersionAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        """"""

    def execute(self, parsed):
        print('Firing version!')
        print(parsed)
