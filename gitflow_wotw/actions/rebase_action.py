# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import InteractiveArgument, PreserveMergesArgument
from gitflow_wotw.components import ActionInstance


class RebaseAction(ActionInstance):
    identifier = 'rebase'
    help_string = 'Rebases a specific branch'

    def __init__(self):
        ActionInstance.__init__(self)
        self.arguments['interactive'] = InteractiveArgument()
        self.arguments['preserve_merges'] = PreserveMergesArgument()
