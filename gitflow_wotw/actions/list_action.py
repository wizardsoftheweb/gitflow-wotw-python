# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class ListAction(ActionInstance):
    identifier = 'list'
    help_string = 'Lists a set of branches'
