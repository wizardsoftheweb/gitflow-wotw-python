# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.constants import PREFIXES
from gitflow_wotw.repo import (
    FlowBranch,
    FlowPrefix,
    FlowPrelaunch,
    FlowRemote,
    FlowTag,
    HasConfig
)


class FlowWrangler(HasConfig):

    def __init__(self, directory=None, config=None):
        HasConfig.__init__(self, directory, config)
        self.branch = FlowBranch(directory, config)
        self.prefix = FlowPrefix(directory, config)
        self.remote = FlowRemote(directory, config)
