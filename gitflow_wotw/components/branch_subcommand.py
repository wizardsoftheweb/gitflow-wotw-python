# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.actions import (
    CheckoutAction,
    DeleteAction,
    DiffAction,
    FinishAction,
    ListAction,
    PublishAction,
    PullAction,
    RebaseAction,
    RenameAction,
    StartAction,
    TrackAction,
)
from gitflow_wotw.components import Subcommand


class BranchSubcommand(Subcommand):

    def __init__(self, subcommand, help_string):
        super(
            BranchSubcommand,
            self
        ).__init__(
            subcommand,
            help_string
        )
        self.populate()

    def populate(self):
        self['list'] = ListAction()
        self['start'] = StartAction()
        self['finish'] = FinishAction()
        self['publish'] = PublishAction()
        self['track'] = TrackAction()
        self['diff'] = DiffAction()
        self['rebase'] = RebaseAction()
        self['rename'] = RenameAction()
        self['checkout'] = CheckoutAction()
        self['pull'] = PullAction()
        self['delete'] = DeleteAction()
