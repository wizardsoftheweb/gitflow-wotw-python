# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.constants import PREFIXES
from gitflow_wotw.repo import HasConfig


class FlowBranch(HasConfig):
    """"""

    def __init__(self, directory=None, config=None):
        HasConfig.__init__(self, directory, config)

    @property
    def master(self):
        return self.config['gitflow.branch.master']

    @property
    def develop(self):
        return self.config['gitflow.branch.develop']

    @property
    def base(self):
        return self.base_from_branch()

    def base_from_branch(self, branch=None):
        if branch is None:
            branch = self.head
        base_key = "gitflow.branch.%s.base" % branch
        if base_key in self.config:
            return self.config[base_key]
        elif branch == self.develop:
            return self.master
        elif branch == self.master:
            return None
        return self.develop

    def update_base(self, branch=None, base=None):
        if branch is None:
            branch = self.head
        if base is None:
            if branch != self.head:
                base = self.head
            else:
                base = self.develop
        print("git config gitflow.branch.%s.base %s" % (branch, base))

    def change_branch(self, branch=None):
        if branch is None:
            branch = self.head
        print("git checkout %s" % branch)

    def change_to_base_branch(self, branch=None):
        if branch is None:
            branch = self.head
        self.change_branch(branch)
