# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Subcommand


class LogSubcommand(Subcommand):
    SUBCOMMAND = 'log'
    HELP_STRING = 'Show log differences (?)'

    def __init__(self):
        super(
            LogSubcommand,
            self
        ).__init__(
            self.SUBCOMMAND,
            self.HELP_STRING
        )
        # print(dir(self))
        # sys_exit(1)
        self.populate()

    def populate(self):
        """"""
