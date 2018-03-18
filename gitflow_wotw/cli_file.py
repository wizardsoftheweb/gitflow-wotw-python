# pylint: disable=W,C,R

from gitflow_wotw.commands import WotwCommand
from time import time as get_time


def cli():
    start = get_time()
    demo = WotwCommand()
    demo.bootstrap()
    end = get_time()
    print(end - start)
