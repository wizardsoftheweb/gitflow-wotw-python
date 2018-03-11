# pylint: disable=missing-docstring

from __future__ import print_function

from gitflow_wotw.constants import HIERARCHY


def test_hierarchy_exists():
    assert len(HIERARCHY) > 1
