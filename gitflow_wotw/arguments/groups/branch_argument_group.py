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
from gitflow_wotw.components import ArgumentGroup


class BranchArgumentGroup(ArgumentGroup):

    def __init__(self):
        ArgumentGroup. __init__(
            self,
            self.__create_seed(),
            'Branch Actions',
            'Keep or delete local and remote branches after the operation finishes',
            False
        )

    def __create_seed(self):
        full = ArgumentGroup(
            seed=OrderedDict({
                'delete': DeleteArgument(),
                'keep': KeepArgument(),
            }),
            exclusive=True
        )
        local = ArgumentGroup(
            seed=OrderedDict({
                'delete': DeleteLocalArgument(),
                'keep': KeepLocalArgument(),
            }),
            exclusive=True
        )
        remote = ArgumentGroup(
            seed=OrderedDict({
                'delete': DeleteRemoteArgument(),
                'keep': KeepRemoteArgument(),
            }),
            exclusive=True
        )
        return OrderedDict({
            'full': full,
            'local': local,
            'remote': remote
        })
