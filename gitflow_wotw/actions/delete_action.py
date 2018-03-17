# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import BranchArgument
from gitflow_wotw.arguments.groups import BranchArgumentGroup
from gitflow_wotw.components import ActionInstance


class DeleteAction(ActionInstance):
    identifier = 'delete'
    help_string = 'Delete a specific branch'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['branch'] = BranchArgument()
        self.arguments['branches'] = BranchArgumentGroup()
        self.post_execution['delete_branch'] = []

    # def execute(self, parsed):
    #     if not parsed.branch:
    #         branch = self.flow_branch.branch
    #     upstream = self.flow_branch.upstream_branch(branch)
    #     self.flow_branch.change_to_base_branch(branch)
    #     if 'local' == parsed.keep:
    #         self.flow_branch.delete_remote_branch(
    #             upstream,
    #             parsed.force
    #         )
    #     elif 'remote' == parsed.keep:
    #         self.flow_branch.delete_local_branch(
    #             branch,
    #             parsed.force
    #         )
    #     elif not parsed.keep or 'both' == parsed.delete:
    #         self.flow_branch.delete_remote_branch(
    #             upstream,
    #             parsed.force
    #         )
    #         self.flow_branch.delete_local_branch(
    #             branch,
    #             parsed.force
    #         )
