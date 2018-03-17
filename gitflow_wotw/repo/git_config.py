# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict

from pygit2 import Config

from gitflow_wotw.utils import HasRepository


class GitConfig(HasRepository, OrderedDict):

    def __init__(self, directory=None):
        OrderedDict.__init__(self)
        HasRepository.__init__(self, directory)
        self.load_and_sort()

    def load_repo_config(self):
        config = {}
        for key in self.repo.config:
            config[key] = self.repo.config[key]
        return config

    def sort_config(self, unsorted_config=None):
        for key in sorted(unsorted_config.iterkeys()):
            self[key] = unsorted_config[key]

    def load_and_sort(self):
        raw = self.load_repo_config()
        self.sort_config(raw)

    @staticmethod
    def dump_config(config=None):
        for key, value in config.items():
            print(key, value)

    @staticmethod
    def global_config():
        return Config.get_global_config()

    @staticmethod
    def system_config():
        return Config.get_system_config()
