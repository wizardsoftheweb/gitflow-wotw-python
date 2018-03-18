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
        self.flow_branch = FlowBranch(directory, config)
        self.flow_prefix = FlowPrefix(directory, config)
