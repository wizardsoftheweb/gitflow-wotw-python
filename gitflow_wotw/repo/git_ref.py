# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

# pylint: disable=no-name-in-module
from pygit2 import GIT_SORT_TOPOLOGICAL
# pylint: enable=no-name-in-module

from gitflow_wotw.constants import FLOWS
from gitflow_wotw.repo import GitConfig
from gitflow_wotw.utils import HasRepository


class GitRef(HasRepository):

    def __init__(self, directory=None):
        super(GitRef, self).__init__(directory)
        self.config = GitConfig(directory)
        self.tags = OrderedDict()
        self.versions = OrderedDict()
        self.remotes = OrderedDict()
        self.local = OrderedDict()
        self.parse_references()

    def parse_references(self):
        for reference in self.repo.references:
            print(reference)
            tag, tag_id = self.check_for_tag(reference)
            if tag or tag_id:
                self.check_for_version_tag(tag, tag_id)

    def check_for_tag(self, reference):
        if reference.startswith('refs/tags/'):
            tag = reference.replace('refs/tags/', '')
            tag_id = self.repo.lookup_reference(reference).peel().id
            self.tags[tag_id] = tag
            return tag, tag_id
        return None, None

    def check_for_version_tag(self, tag=None, tag_id=None):
        if not self.config.version_tag is None:
            if tag.startswith(self.config.version_tag):
                self.versions[tag_id] = tag.replace(
                    self.config.version_tag,
                    '',
                    1
                )

    def check_for_local(self, reference=None):
        if reference.startswith('refs/heads/'):
            branch = reference.replace('refs/heads/')
            self.local[branch] = self.repo.lookup_reference(reference).peel()

    def check_for_remote(self, reference):
        if reference.startswith('refs/remotes/'):
            remote_reference = reference.replace('refs/remotes/')
            chunks = remote_reference.split('/')
            if chunks[0] in self.remotes:
                self.remotes[chunks[0]].append(chunks[1:].join('/'))
            else:
                self.remotes[chunks[0]] = [chunks[1:].join('/')]

    def active_branch(self):
        if self.repo.head_is_detached or self.repo.head_is_unborn:
            return None
        return self.repo.head.name.replace('refs/heads/', '')

    def flow_from_branch(self, branch=None):
        chunks = branch.split('/')
        if self.is_valid_flow(chunks[0]):
            return chunks[0]
        return None

    def base_from_branch(self, branch=None):
        production = self.config['gitflow.branch.master']
        develop = self.config['gitflow.branch.develop']
        if branch == production:
            return None
        elif branch == develop:
            return production
        elif self.config["gitflow.branch.%s.base" % branch]:
            return self.config["gitflow.branch.%s.base" % branch]
        return develop

    def active_flow_and_branch(self):
        branch = self.active_branch()
        flow = self.flow_from_branch(branch)
        return flow, branch

    def is_valid_flow(self, flow=None):
        return self.is_vanilla_flow(flow) or self.is_user_flow(flow)

    @staticmethod
    def is_vanilla_flow(flow=None):
        return flow in FLOWS

    def is_user_flow(self, flow=None):
        return flow in self.config.prefixes.itervalues()

    def walk_for_tags(self):
        last = None
        version = None
        for commit in self.repo.walk(self.repo.head.target, GIT_SORT_TOPOLOGICAL):
            if not last and commit.id in self.tags:
                last = self.tags[commit.id]
            if not version and commit.id in self.versions:
                version = self.versions[commit.id]
            if last and version:
                break
        return last, version

    def important_refs(self):
        flow, branch = self.active_flow_and_branch()
        base = self.base_from_branch(branch)
        tag, version = self.walk_for_tags()
        return OrderedDict({
            'flow': flow,
            'branch': branch,
            'base': base,
            'tag': tag,
            'version': version
        })
