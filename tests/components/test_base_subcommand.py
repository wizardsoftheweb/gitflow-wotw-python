# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw.components import Subcommand


class SubcommandTestCase(TestCase):

    def setUp(self):
        self.construct_base_subcommand()
        self.addCleanup(self.wipe_base_subcommand)

    def wipe_base_subcommand(self):
        del self.base_subcommand

    def construct_base_subcommand(self):
        self.base_subcommand = Subcommand()


class ConstructorUnitTests(SubcommandTestCase):

    def setUp(self):
        SubcommandTestCase.setUp(self)


class AttachBelowUnitTests(SubcommandTestCase):

    def setUp(self):
        SubcommandTestCase.setUp(self)


class PrintHelpBelowUnitTests(SubcommandTestCase):

    def setUp(self):
        SubcommandTestCase.setUp(self)
