# pylint:disable=W,C,R

from __future__ import print_function

from os import mkdir
from os.path import join

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
        self.arguments['branches'] = BranchArgumentGroup()
        # self.arguments['tag'] = TagArgumentGroup()
        self.arguments['push'] = PushArgumentGroup()
        self.arguments['fetch'] = FetchArgument()
        self.arguments['rebase'] = RebaseArgument()
        self.arguments['preserve_merges'] = PreserveMergesArgument()
        self.arguments['squash'] = SquashArgument()
        self.arguments['ff'] = FfArgument()
        self.post_execution['push_results'] = []
        self.post_execution['delete_branch'] = []
        # self.arguments['ff_master'] = FfMasterArgument()
        # self.arguments['back_merge'] = BackMergeArgument()

    def execute(self, parsed):
        print('firing!')
        self.fetch_first(parsed)
        self.stream_equality(parsed)
        self.rebase_first(parsed)
        self.finish_with_failsafe(parsed)

    def tidy_branch(self, parsed):
        if not parsed.branch:
            parsed.branch = self.flow_branch.branch

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

    def rebase_first(self, parsed):
        if parsed.rebase:
            options = ''
            if parsed.preserve_merges:
                options += ' --preserve-merges'
            print(
                "git flow feature rebase%s %s" % (
                    options,
                    parsed.branch
                )
            )

    def merge_without_squash(self, parsed):
        print("git merge --no-ff %s" % parsed.branch)

    def merge_with_squash(self, parsed):
        print("git merge --squash %s" % parsed.branch)
        print("git commit")

    def change_and_merge(self, parsed):
        self.flow_branch.change_to_base_branch(parsed.branch)
        if parsed.squash:
            self.merge_with_squash(parsed)
        else:
            self.merge_without_squash(parsed)

    def handle_merge_error(self, parsed):
        directory = join(
            self.flow_branch.repo.path,
            '.gitflow'
        )
        mkdir(directory)
        with open(join(directory, 'MERGE_BASE'), 'w') as merge_file:
            merge_file.write(self.flow_branch.base_branch(parsed.branch))
        raise RuntimeError(
            'Merge conflict detected; please fix before continuing'
        )

    def finish_with_failsafe(self, parsed):
        try:
            self.change_and_merge(parsed)
        except Exception as e:
            # TODO: need to figure out the real exception
            print(e)
            self.handle_merge_error(parsed)
