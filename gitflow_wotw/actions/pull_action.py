# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Action


class PullAction(Action):
    ACTION = 'pull'
    HELP_STRING = 'Pulles a specific branch'

    def __init__(self):
        super(PullAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        """"""

    def execute(self, parsed):
        print('Firing pull!')
        print(parsed)
