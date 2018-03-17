# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    DeleteArgument,
    DeleteLocalArgument,
    DeleteRemoteArgument,
    FetchArgument,
    FfArgument,
    ForceArgument,
    KeepArgument,
    KeepLocalArgument,
    KeepRemoteArgument,
    PushArgument,
    PushDevelopArgument,
    PushProductionArgument,
    PushTagArgument,
    PreserveMergesArgument,
    RebaseArgument,
    ShowCommandsArgument,
    SquashArgument
)
from gitflow_wotw.components import Action


class FinishAction(Action):
    ACTION = 'finish'
    HELP_STRING = 'Finish a specific something'

    def __init__(self):
        super(FinishAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['fetch'] = FetchArgument()
        self.arguments['rebase'] = RebaseArgument()
        self.arguments['preserve_merges'] = PreserveMergesArgument()
        self.exclusive_groups.append([
            DeleteArgument(),
            KeepArgument()
        ])
        self.exclusive_groups.append([
            DeleteLocalArgument(),
            KeepLocalArgument()
        ])
        self.exclusive_groups.append([
            DeleteRemoteArgument(),
            KeepRemoteArgument()
        ])
        self.arguments['push'] = PushArgument()
        self.arguments['push_develop'] = PushDevelopArgument()
        self.arguments['push_master'] = PushProductionArgument()
        self.arguments['push_tag'] = PushTagArgument()
        self.arguments['force'] = ForceArgument()
        self.arguments['squash'] = SquashArgument()
        self.arguments['ff'] = FfArgument()
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing finish!')
        print(parsed)
