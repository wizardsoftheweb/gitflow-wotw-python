# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class PublishAction(ActionInstance):
    identifier = 'publish'
    help_string = 'Publish a specific branch'
