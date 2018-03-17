# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class TrackAction(ActionInstance):
    identifier = 'track'
    help_string = 'Tracks a specific branch'
