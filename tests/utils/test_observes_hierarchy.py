# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw.utils import ObservesHierarchy


class ObservesHierarchyTestCase(TestCase):

    def setUp(self):
        self.construct_observes_hierarchy()
        self.addCleanup(self.wipe_observes_hierarchy)

    def wipe_observes_hierarchy(self):
        del self.observes_hierarchy

    def construct_observes_hierarchy(self):
        self.observes_hierarchy = ObservesHierarchy()


class ConstructorUnitTests(ObservesHierarchyTestCase):

    def setUp(self):
        ObservesHierarchyTestCase.setUp(self)


class ValidateTierUnitTests(ObservesHierarchyTestCase):

    def setUp(self):
        ObservesHierarchyTestCase.setUp(self)


class DetermineAboveUnitTests(ObservesHierarchyTestCase):

    def setUp(self):
        ObservesHierarchyTestCase.setUp(self)


class DetermineBelowUnitTests(ObservesHierarchyTestCase):

    def setUp(self):
        ObservesHierarchyTestCase.setUp(self)


class ConsumeHierarchyUnitTests(ObservesHierarchyTestCase):

    def setUp(self):
        ObservesHierarchyTestCase.setUp(self)
