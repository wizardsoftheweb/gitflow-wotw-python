# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.arguments import FetchArgument
from gitflow_wotw.components import ActionInstance


class StartAction(ActionInstance):
    identifier = 'start'
    help_string = 'Start a new something'
