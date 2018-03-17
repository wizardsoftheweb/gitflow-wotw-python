# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Subcommand


class InitSubcommand(Subcommand):
    SUBCOMMAND = 'init'
    HELP_STRING = 'Initializes gitflow'

    def __init__(self):
        super(
            InitSubcommand,
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
