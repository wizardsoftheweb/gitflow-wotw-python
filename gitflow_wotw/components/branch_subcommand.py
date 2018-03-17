# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.actions import (
    StartAction,
    FinishAction,
    PublishAction,
    TrackAction,
    DiffAction,
    RebaseAction,
    RenameAction,
    CheckoutAction,
    PullAction,
    DeleteAction,
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
