# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from subprocess import check_output

from gitflow_wotw.utils import HasRepository
from re import compile as re_compile, finditer, MULTILINE, VERBOSE


class GitConfig(OrderedDict, HasRepository):
    CONFIG_LINE_PATTERN = re_compile(
        r"""
        ^\s*(?P<key>.*?)=(?P<value>.*?)\s*$
        """,
        MULTILINE | VERBOSE
    )

    def __init__(self, directory=None):
        OrderedDict.__init__(self)
        HasRepository.__init__(self, directory)
        self.load_and_sort()

    def __missing__(self, key):
        return 'qqq'

    @staticmethod
    def get_active_config():
        return check_output([
            'git',
            'config',
            '--list'
        ]).strip()

    def parse_config(self, config_to_parse):
        config = {}
        for matched in finditer(GitConfig.CONFIG_LINE_PATTERN, config_to_parse):
            key = matched.group('key')
            value = matched.group('value')
            config[key] = value
        return config

    def sort_config(self, unsorted_config=None):
        for key in sorted(unsorted_config.iterkeys()):
            self[key] = unsorted_config[key]

    def load_and_sort(self):
        raw = self.get_active_config()
        config = self.parse_config(raw)
        self.sort_config(config)

    @staticmethod
    def dump_config(config=None):
        for key, value in config.items():
            print(key, value)
