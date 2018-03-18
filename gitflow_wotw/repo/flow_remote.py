# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from subprocess import check_output

from gitflow_wotw.constants import PREFIXES
from gitflow_wotw.repo import HasConfig


class FlowRemote(HasConfig):
    """"""

    # def __init__(self, directory=None, config=None):
    #     super(FlowBranch, self).__init__(directory, config)
    #     self.stored_prefixes = []
    #     self.branch = self.repo.head.shorthand
    #     self.all_branches = self.sort_branches()

    def list_local(self, prefix=None):
        return check_output([
            'git',
            'for-each-ref',
            '--format',
            '%(refname:lstrip=3)',
            "refs/heads%s" % prefix
        ]).strip().split('\n')

    def list_remote(self, prefix=None):
        results = OrderedDict()
        branches = check_output([
            'git',
            'for-each-ref',
            '--format',
            '%(refname:lstrip=2)',
            'refs/remotes'
        ]).strip().split('\n')
        remotes = check_output(['git', 'remote']).strip().split('\n')
        for remote in remotes:
            unclaimed = []
            results[remote] = []
            for branch in branches:
                if branch.startswith(remote):
                    remote_branch = branch.replace(remote, '', 1)[1:]
                    if prefix:
                        if remote_branch.startswith(prefix):
                            results[remote].append(
                                remote_branch.replace(prefix, '', 1)[1:]
                            )
                    else:
                        results[remote].append(remote_branch)
        return results

    def upstream_from_branch(self, branch=None):
        if branch is None:
            branch = self.branch
        return self.config["branch.%s.merge" % branch]

    @property
    def upstream(self):
        return self.upstream_from_branch()

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

    def strip_remote_from_ref(self, upstream=None):
        return upstream.replace('refs/heads/', '')

    def delete_remote_branch(self, upstream=None, force=False):
        if upstream:
            branch = self.strip_remote_from_ref(upstream)
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

    def fetch_if_upstream(self, branch=None):
        upstream = self.upstream_from_branch(branch)
        if upstream:
            print(
                "git fetch %s %s" % (
                    upstream.remote_name,
                    self.strip_remote_from_ref(upstream)
                )
            )

    def hash_from_branch(self, branch=None):
        if branch is None:
            branch = self.branch
        return check_output(['git', 'rev-parse', '--short', branch]).strip()

    def compare_references(self, first_branch=None, second_branch=None):
        first_commit = self.hash_from_branch(first_branch)
        second_commit = self.hash_from_branch(second_branch)
        if first_commit != second_commit:
            base = check_output([
                'git',
                'merge-base',
                first_commit,
                second_commit
            ]).strip()
            if base == second_commit:
                return 1
            else:
                return 2
        return 0

    def ensure_local_and_remote_equal(self, branch=None):
        if branch is None:
            branch = self.branch
        upstream = self.upstream_from_branch(branch)
        if not upstream:
            return True
        result = self.compare_references(branch, upstream)
        if result > 1 or result < 0:
            raise ValueError(
                'Local and remote have diverged; a merge is necessary'
            )
        return True
