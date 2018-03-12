# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import Command


class CommandTestCase(TestCase):

    def setUp(self):
        self.construct_command()
        self.addCleanup(self.wipe_command)

    def wipe_command(self):
        del self.command

    def construct_command(self):
        self.command = Command()


class ConstructorUnitTests(CommandTestCase):

    def setUp(self):
        CommandTestCase.setUp(self)


class BootstrapUnitTests(CommandTestCase):

    def setUp(self):
        CommandTestCase.setUp(self)
