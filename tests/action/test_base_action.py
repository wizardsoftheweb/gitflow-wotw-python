# pylint: disable=missing-docstring

from __future__ import print_function

from gitflow_wotw.action import Action


def test_execute_exists():
    action = Action()
    assert hasattr(action, 'execute')
