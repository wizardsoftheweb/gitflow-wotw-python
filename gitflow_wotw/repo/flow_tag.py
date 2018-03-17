# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

# pylint: disable=no-name-in-module
from pygit2 import GIT_SORT_TOPOLOGICAL
# pylint: enable=no-name-in-module

from gitflow_wotw.repo import HasConfig


class FlowTag(HasConfig):

    def __init__(self, directory=None, config=None):
        super(FlowTag, self).__init__(directory, config)
        self.tags = OrderedDict()
        self.versions = OrderedDict()
        self.parse_tags()

    @property
    def version_tag(self):
        return (
            'gitflow.prefix.versiontag' in self.config
            and
            self.config['gitflow.prefix.versiontag'].encode('utf-8')
        )

    def parse_tags(self):
        for reference in [
                reference
                for reference in self.repo.references
                if reference.startswith('refs/tags/')
        ]:
            tag = reference.replace('refs/tags/', '')
            tag_id = self.repo.lookup_reference(reference).peel().id
            if self.version_tag and tag.startswith(self.version_tag):
                self.versions[tag_id] = tag.replace(self.version_tag, '', 1)
            self.tags[tag_id] = tag

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
