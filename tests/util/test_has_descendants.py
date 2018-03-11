# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import HasDescendants


class HasDescendantsTestCase(TestCase):

    def setUp(self):
        self.construct_has_descendants()
        self.addCleanup(self.wipe_has_descendants)

    def wipe_has_descendants(self):
        del self.has_descendants

    def construct_has_descendants(self):
        self.has_descendants = HasDescendants()


class ConstructorUnitTests(HasDescendantsTestCase):

    def setUp(self):
        HasDescendantsTestCase.setUp(self)


class AddDescendantUnitTests(HasDescendantsTestCase):

    def setUp(self):
        HasDescendantsTestCase.setUp(self)


class ExecuteUnitTests(HasDescendantsTestCase):

    def setUp(self):
        HasDescendantsTestCase.setUp(self)
