# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import (
    BackMergeArgument,
    BranchArgument,
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
        self.arguments['branch'] = BranchArgument()
        # self.arguments['branches'] = BranchArgumentGroup()
        # self.arguments['tag'] = TagArgumentGroup()
        # self.arguments['push'] = PushArgumentGroup()
        self.arguments['fetch'] = FetchArgument()
        # self.arguments['rebase'] = RebaseArgument()
        # self.arguments['preserve_merges'] = PreserveMergesArgument()
        # self.arguments['squash'] = SquashArgument()
        # self.arguments['ff'] = FfArgument()
        # self.arguments['ff_master'] = FfMasterArgument()
        # self.arguments['back_merge'] = BackMergeArgument()

    def execute(self, parsed):
        print('firing!')
        self.fetch_first(parsed)

    def pretasks(self):
        print('run before merge')

    def fetch_first(self, parsed):
        self.flow_branch.fetch_if_upstream(parsed.branch)
        if parsed.fetch:
            self.flow_branch.fetch_if_upstream(
                self.flow_branch.base_branch(parsed.branch)
            )

    def stream_equality(self, parsed):
        self.flow_branch.ensure_local_and_remote_equal(parsed.branch)
