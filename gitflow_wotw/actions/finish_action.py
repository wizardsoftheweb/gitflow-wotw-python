# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    BackMergeArgument,
    DeleteArgument,
    DeleteLocalArgument,
    DeleteRemoteArgument,
    FetchArgument,
    FfArgument,
    FfMasterArgument,
    ForceArgument,
    KeepArgument,
    KeepLocalArgument,
    KeepRemoteArgument,
    MessageArgument,
    MessageFileArgument,
    PushArgument,
    PushDevelopArgument,
    PushProductionArgument,
    PushTagArgument,
    PreserveMergesArgument,
    RebaseArgument,
    ShowCommandsArgument,
    SignArgument,
    SigningKeyArgument,
    SquashArgument,
    TagArgument,
    TagNameArgument
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
        self.arguments['sign'] = SignArgument()
        self.arguments['signing_key'] = SigningKeyArgument()
        self.arguments['tag'] = TagArgument()
        self.arguments['tag_name'] = TagNameArgument()
        self.exclusive_groups.append([
            MessageArgument(),
            MessageFileArgument()
        ])
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
        self.arguments['ff_master'] = FfMasterArgument()
        self.arguments['back_merge'] = BackMergeArgument()
        self.arguments['show_commands'] = ShowCommandsArgument()

    def execute(self, parsed):
        print('Firing finish!')
        print(parsed)
