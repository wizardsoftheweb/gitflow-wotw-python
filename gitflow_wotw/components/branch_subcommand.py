# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.actions import (
    CheckoutAction,
    DeleteAction,
    DiffAction,
    FinishAction,
    ListAction,
    PublishAction,
    RebaseAction,
    RenameAction,
    StartAction,
    TrackAction,
)
from gitflow_wotw.components import SubcommandInstance


class BranchSubcommand(SubcommandInstance):

    def __init__(self):
        SubcommandInstance.__init__(self)
        self['list'] = ListAction()
        self['start'] = StartAction()
        self['finish'] = FinishAction()
        self['publish'] = PublishAction()
        self['track'] = TrackAction()
        self['diff'] = DiffAction()
        self['rebase'] = RebaseAction()
        self['rename'] = RenameAction()
        self['checkout'] = CheckoutAction()
        self['delete'] = DeleteAction()
