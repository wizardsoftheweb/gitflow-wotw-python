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
from gitflow_wotw.components import ActionInstance


class FinishAction(ActionInstance):
    identifier = 'finish'
    help_string = 'Finish a specific something'

    def __init__(self):
        ActionInstance.__init__(self)
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
