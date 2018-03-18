# pylint:disable=W,C,R

from gitflow_wotw.generators import ObjectBuilder


def cli():
    builder = ObjectBuilder()
    WotwCommand = builder('WotwCommand')
    WotwCommand()
