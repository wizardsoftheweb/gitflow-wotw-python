# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    DeleteArgument,
    DeleteLocalArgument,
    DeleteRemoteArgument,
    KeepArgument,
    KeepLocalArgument,
    KeepRemoteArgument,
    ForceArgument,
    ShowCommandsArgument
)
from gitflow_wotw.components import Action


class DeleteAction(Action):
    ACTION = 'delete'
    HELP_STRING = 'Delete a specific branch'

    def __init__(self):
        super(DeleteAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['delete'] = DeleteArgument()
        self.arguments['delete_local'] = DeleteLocalArgument()
        self.arguments['delete_remote'] = DeleteRemoteArgument()
        self.arguments['keep'] = KeepArgument()
        self.arguments['keep_local'] = KeepLocalArgument()
        self.arguments['keep_remote'] = KeepRemoteArgument()
        self.arguments['force'] = ForceArgument()
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing delete!')
        print(parsed)
