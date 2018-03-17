# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

# pylint: disable=no-name-in-module
from pygit2 import GIT_SORT_TOPOLOGICAL
# pylint: enable=no-name-in-module

from gitflow_wotw.constants import FLOWS
from gitflow_wotw.repo import HasConfig


class GitRef(HasConfig):

    def __init__(self, directory=None, config=None):
        super(GitRef, self).__init__(directory, config)
        self.tags = OrderedDict()
        self.versions = OrderedDict()
        self.parse_references()

    def parse_references(self):
        for reference in self.repo.references:
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
        # flow, branch = self.active_flow_and_branch()
        # base = self.base_from_branch(branch)
        tag, version = self.walk_for_tags()
        # return OrderedDict({
        #     'flow': flow,
        #     'branch': branch,
        #     'base': base,
        #     'tag': tag,
        #     'version': version
        # })
