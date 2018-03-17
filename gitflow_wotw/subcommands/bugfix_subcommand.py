# pylint: disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import Subcommand


class BugfixSubcommand(Subcommand):
    SUBCOMMAND = 'bugfix'
    HELP_STRING = 'Manages bugfix branches'

    def __init__(self):
        super(
            BugfixSubcommand,
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
