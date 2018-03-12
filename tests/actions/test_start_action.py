# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw.actions import StartAction


class StartActionTestCase(TestCase):

    def setUp(self):
        self.construct_start_action()
        self.addCleanup(self.wipe_start_action)

    def wipe_start_action(self):
        del self.start_action

    def construct_start_action(self):
        self.start_action = StartAction()


class ConstructorUnitTests(StartActionTestCase):

    def setUp(self):
        StartActionTestCase.setUp(self)


class ExecuteUnitTests(StartActionTestCase):

    def setUp(self):
        StartActionTestCase.setUp(self)
