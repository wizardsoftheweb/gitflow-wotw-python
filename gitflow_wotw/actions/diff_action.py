# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class DiffAction(ActionInstance):
    identifier = 'diff'
    help_string = 'Compare the branch against its base'
