# pylint: disable=W,C,R

from gitflow_wotw.commands import WotwCommand


def cli():
    demo = WotwCommand()
    demo.bootstrap()
