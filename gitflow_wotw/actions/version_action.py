# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class VersionAction(ActionInstance):
    identifier = 'version'
    help_string = 'List program version'
