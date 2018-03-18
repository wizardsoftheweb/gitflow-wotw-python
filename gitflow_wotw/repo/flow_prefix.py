# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.constants import PREFIXES
from gitflow_wotw.repo import HasConfig


class FlowPrefix(HasConfig):
    """"""

    def __init__(self, directory=None, config=None):
        HasConfig.__init__(self, directory, config)
        self.stored_prefixes = []

    @staticmethod
    def is_prefix(prefix):
        return prefix in PREFIXES

    @staticmethod
    def validate_prefix(prefix):
        if not FlowPrefix.is_prefix(prefix):
            raise KeyError("'%s' is not a valid gitflow prefix")

    @property
    def prefixes(self):
        if not self.stored_prefixes:
            for prefix in PREFIXES:
                self.stored_prefixes.append(
                    self.config["gitflow.prefix.%s" % prefix]
                )
        return self.stored_prefixes

    def prefix_from_branch(self, branch=None):
        if branch is None:
            branch = self.branch
        for prefix in self.prefixes:
            if branch.startswith(prefix):
                return prefix[0:-1]
        return None

    @property
    def prefix(self):
        return self.prefix_from_branch()
