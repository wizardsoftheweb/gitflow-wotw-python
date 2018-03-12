# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw.components import Argument


class ArgumentTestCase(TestCase):

    def setUp(self):
        self.construct_base_argument()
        self.addCleanup(self.wipe_base_argument)

    def wipe_base_argument(self):
        del self.base_argument

    def construct_base_argument(self):
        self.base_argument = Argument()


class ConstructorUnitTests(ArgumentTestCase):

    def setUp(self):
        ArgumentTestCase.setUp(self)


class AttachArgumentUnitTests(ArgumentTestCase):

    def setUp(self):
        ArgumentTestCase.setUp(self)
