# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from pygit2 import Config

from gitflow_wotw.repo import HasConfig


class FlowPrelaunch(HasConfig):

    def __init__(self, directory=None, config=None):
        super(FlowPrelaunch, self).__init__(directory, config)
        if not self.all_branches_configured():
            self.kill_process()

    def branch_configured(self, branch):
        key = "gitflow.branch.%s" % branch
        return (
            key in self.config
            and
            self.repo.branches.get(self.config[key])
            and
            self.config[key]
        )

    def all_branches_configured(self):
        develop = self.branch_configured('develop')
        master = self.branch_configured('master')
        return develop and master and develop != master

    def kill_process(self):
        raise RuntimeError(
            'Not a gitflow-enabled repo; run `git flow init` first'
        )
