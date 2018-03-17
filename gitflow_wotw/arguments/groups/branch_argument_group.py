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
