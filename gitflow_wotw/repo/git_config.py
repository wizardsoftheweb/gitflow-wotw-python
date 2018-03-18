# pylint: disable=W,C,R

from __future__ import print_function

from collections import OrderedDict
from subprocess import check_output

from gitflow_wotw.utils import HasRepository
from re import compile as re_compile, match, MULTILINE, VERBOSE


class GitConfig(HasRepository, OrderedDict):
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

    @staticmethod
    def get_active_config():
        return check_output([
            'git',
            'config',
            '--list'
        ]).strip().split('\n')

    def parse_config(self, config_to_parse):
        for row in config_to_parse:
            matched = match(GitConfig.CONFIG_LINE_PATTERN, row)
            if matched:
                key = matched.group('key')
                value = matched.group('value')
                if key in self:
                    if isinstance(self[key], list):
                        self[key] = self[key] + [value]
                    else:
                        self[key] = [self[key], value]
                else:
                    self[key] = value

    def load_and_sort(self):
        raw = self.get_active_config()
        self.parse_config(raw)

    @staticmethod
    def dump_config(config=None):
        for key, value in config.items():
            print(key, value)
