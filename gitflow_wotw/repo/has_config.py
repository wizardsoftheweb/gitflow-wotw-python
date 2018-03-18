# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from gitflow_wotw.repo import GitConfig
from gitflow_wotw.utils import HasRepository


class HasConfig(HasRepository):

    def __init__(self, directory=None, config=None):
        HasRepository.__init__(self, directory, config)
        if isinstance(config, GitConfig):
            self.config = config
        else:
            self.config = GitConfig(directory)
