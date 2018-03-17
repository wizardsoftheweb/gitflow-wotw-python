# pylint:disable=W,C,R

from __future__ import print_function

from gitflow_wotw.components import ActionInstance


class CheckoutAction(ActionInstance):
    identifier = 'checkout'
    help_string = 'Check out a specific branch'
