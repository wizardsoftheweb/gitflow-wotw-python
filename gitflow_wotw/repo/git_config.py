# pylint: disable=W,C,R

from __future__ import print_function

from pygit2 import config

from gitflow_wotw.utils import HasRepository


class GitConfig(HasRepository):

    def __init__(self, directory=None):
        super(GitConfig, self).__init__(directory)
        print(self.repo.config)
