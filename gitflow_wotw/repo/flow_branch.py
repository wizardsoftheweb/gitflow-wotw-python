# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from pygit2 import Config

from gitflow_wotw.constants import FLOWS
from gitflow_wotw.repo import HasConfig


class FlowBranch(HasConfig):

    def __init__(self, directory=None, config=None):
        super(FlowBranch, self).__init__(directory, config)
        self.stored_prefixes = []
        self.branch = self.repo.head.shorthand
        self.all_branches = self.sort_branches()

    def sort_branches(self):
        branches = OrderedDict()
        branches['local'] = self.sort_local_branches()
        branches['remote'] = self.sort_remote_branches()
        return branches

    def sort_local_branches(self, available_branches=None):
        if available_branches is None:
            available_branches = list(self.repo.branches.local)
        prefixed, not_prefixed = self.sort_by_prefixes(
            available_branches,
            self.prefixes
        )
        prefixed['none'] = not_prefixed
        return prefixed

    def sort_remote_branches(self):
        available_branches = list(self.repo.branches.remote)
        remotes = [
            "%s/" % remote.name
            for remote
            in self.repo.remotes
        ]
        prefixed, _ = self.sort_by_prefixes(
            available_branches,
            remotes,
            self.sort_local_branches
        )
        return prefixed

    @staticmethod
    def sort_by_prefixes(branches=None, prefixes=None, callback=None):
        if not callable(callback):
            callback = lambda x: x
        prefixed_lists = OrderedDict()
        for prefix in prefixes:
            prefixed, unclaimed = FlowBranch.check_for_prefix(
                branches,
                prefix
            )
            prefixed_lists[prefix[0:-1]] = callback(prefixed)
            branches = unclaimed
        return prefixed_lists, branches

    @staticmethod
    def check_for_prefix(branches=None, prefix=None):
        prefixed = []
        not_prefixed = []
        for branch in branches:
            if branch.startswith(prefix):
                prefixed.append(branch.replace(prefix, '').encode('utf-8'))
            else:
                not_prefixed.append(branch)
        return prefixed, not_prefixed

    def list(self, prefix=None, include_remotes=False):
        if prefix is None:
            prefix = 'none'
        else:
            self.validate_flow(prefix)
        branches = self.all_branches['local'][prefix]
        if include_remotes:
            for remote in self.all_branches['remote']:
                branches = (
                    branches + [
                        "%s/%s" % (remote, branch)
                        for branch
                        in self.all_branches['remote'][remote][prefix]
                    ]
                )
        return branches

    @staticmethod
    def is_flow(flow):
        return flow in FLOWS

    @staticmethod
    def validate_flow(flow):
        if not FlowBranch.is_flow(flow):
            raise KeyError("'%s' is not a valid gitflow prefix")

    @property
    def prefixes(self):
        if not self.stored_prefixes:
            for flow in FLOWS:
                self.stored_prefixes.append(
                    self.config["gitflow.prefix.%s" % flow]
                )
        return self.stored_prefixes

    @property
    def master(self):
        return self.config['gitflow.branch.master']

    @property
    def develop(self):
        return self.config['gitflow.branch.develop']

    @property
    def current_base(self):
        return self.base_branch()

    def upstream_branch(self, branch=None):
        if branch is None:
            branch = self.branch
        return self.repo.branches[branch].upstream

    @property
    def upstream(self):
        return self.repo.branches[self.branch].upstream

    @property
    def current_flow(self):
        for prefix in self.prefixes:
            if self.branch.startswith(prefix):
                return prefix[0:-1]
        return None

    def base_branch(self, branch=None):
        if branch is None:
            branch = self.branch
        base_key = "gitflow.branch.%s.base" % branch
        print("git config --get gitflow.branch.%s.base" % branch)
        if base_key in self.config:
            return self.config[base_key]
        elif branch == self.develop:
            return self.master
        elif branch == self.master:
            return None
        return self.develop

    def update_base(self, branch=None, base=None):
        if branch is None:
            branch = self.branch
        if base is None:
            if branch != self.branch:
                base = self.branch
            else:
                base = self.develop
        print("git config gitflow.branch.%s.base %s" % (branch, base))

    def branch_to_reference(self, branch=None):
        if branch is None:
            branch = self.branch
        try:
            prefixed_branch = "%s/%s" % (self.current_flow, branch)
            branch_object = self.repo.branches[prefixed_branch]
        except KeyError:
            branch_object = self.repo.branches[branch]
        return self.repo.lookup_reference(branch_object.name)

    def change_branch(self, branch=None):
        reference = self.branch_to_reference(branch)
        print("git checkout %s" % reference.shorthand)
        # self.repo.checkout(reference)

    def change_branch_if_active(self, branch=None):
        if branch is None:
            branch = self.branch
        if self.repo.branches[branch].is_head():
            self.change_to_base_branch(branch)

    def change_to_base_branch(self, branch=None):
        self.change_branch(self.base_branch(branch))

    def delete_local_branch(self, branch=None, force=False):
        print(
            "git branch%s -d %s" % (
                (
                    ' --force'
                    if force
                    else ''
                ),
                branch
            )
        )
        # self.repo.branches[branch].delete()

    def delete_remote_branch(self, upstream=None, force=False):
        branch = upstream.shorthand.replace("%s/" % upstream.remote_name, '')
        print(
            "git push%s %s :%s" % (
                (
                    ' --force'
                    if force
                    else ''
                ),
                upstream.remote_name,
                branch
            )
        )
