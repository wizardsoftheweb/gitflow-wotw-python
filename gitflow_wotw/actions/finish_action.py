# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    BackMergeArgument,
    FetchArgument,
    FfArgument,
    FfMasterArgument,
    PreserveMergesArgument,
    RebaseArgument,
    SquashArgument,
)
from gitflow_wotw.arguments.groups import (
    BranchArgumentGroup,
    PushArgumentGroup,
    TagArgumentGroup
)
from gitflow_wotw.components import Action


class FinishAction(Action):
    ACTION = 'finish'
    HELP_STRING = 'Finish a specific something'

    def __init__(self):
        super(FinishAction, self).__init__(self.ACTION, self.HELP_STRING)
        self.populate()

    def populate(self):
        self.arguments['branch'] = BranchArgumentGroup()
        self.arguments['tag'] = TagArgumentGroup()
        self.arguments['push'] = PushArgumentGroup()
        self.arguments['fetch'] = FetchArgument()
        self.arguments['rebase'] = RebaseArgument()
        self.arguments['preserve_merges'] = PreserveMergesArgument()
        self.arguments['squash'] = SquashArgument()
        self.arguments['ff'] = FfArgument()
        self.arguments['ff_master'] = FfMasterArgument()
        self.arguments['back_merge'] = BackMergeArgument()

    def execute(self, parsed):
        print('Firing finish!')
        print(parsed)
