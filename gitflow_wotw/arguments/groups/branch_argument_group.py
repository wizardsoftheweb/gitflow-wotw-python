# pylint: disable=W,C,R

from collections import OrderedDict

from gitflow_wotw.arguments import (
    DeleteArgument,
    DeleteLocalArgument,
    DeleteRemoteArgument,
    KeepArgument,
    KeepLocalArgument,
    KeepRemoteArgument
)
from gitflow_wotw.components import ArgumentGroup, ArgumentGroupInstance


class BranchArgumentGroup(ArgumentGroupInstance):
    seed = OrderedDict()
    seed['full'] = ArgumentGroup(
        seed=OrderedDict({
            'delete': DeleteArgument(),
            'keep': KeepArgument(),
        }),
        exclusive=True
    )
    seed['local'] = ArgumentGroup(
        seed=OrderedDict({
            'delete': DeleteLocalArgument(),
            'keep': KeepLocalArgument(),
        }),
        exclusive=True
    )
    seed['remote'] = ArgumentGroup(
        seed=OrderedDict({
            'delete': DeleteRemoteArgument(),
            'keep': KeepRemoteArgument(),
        }),
        exclusive=True
    )
    title = 'Branch Actions'
    help_string = 'Keep or delete local and remote branches after the operation finishes'
    exclusive = False

    def __init__(self):
        ArgumentGroupInstance.__init__(self)
        self.handlers['delete_branch'] = self.delete_branch

    @staticmethod
    def delete_branch(runner, parsed):
        runner.handlers['change_to_base_branch'](runner, parsed)
        if 'local' == parsed.keep:
            runner.flow.branch.delete_remote_branch(
                parsed.upstream,
                parsed.force
            )
        elif 'remote' == parsed.keep:
            runner.flow.branch.delete_local_branch(
                parsed.branch,
                parsed.force
            )
        elif not parsed.keep or 'both' == parsed.delete:
            runner.flow.branch.delete_remote_branch(
                parsed.upstream,
                parsed.force
            )
            runner.flow.branch.delete_local_branch(
                parsed.branch,
                parsed.force
            )
