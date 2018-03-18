# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from subprocess import check_output

from gitflow_wotw.repo import HasConfig


class FlowTag(HasConfig):
    """"""

    def __init__(self, directory=None, config=None):
        super(FlowTag, self).__init__(directory, config)
        self.tags = OrderedDict()
        self.versions = OrderedDict()

    @property
    def tag(self):
        return check_output(['git', 'describe', '--abbrev', ' 0']).strip()

    @property
    def version_tag(self):
        return self.config['gitflow.prefix.versiontag']

    def parse_tags(self):
        tags = check_output([
            'git',
            'show-ref',
            '--tags',
            '--abbrev'
        ]).strip().split('\n')
        for tag in tags:
            explode = tag.split(' ').strip()
            tag_id = explode[0]
            tag = explode[1].replace('refs/tags/', '')
            if self.version_tag and tag.startswith(self.version_tag):
                self.versions[tag_id] = tag.replace(self.version_tag, '')
            self.tags[tag_id] = tag
