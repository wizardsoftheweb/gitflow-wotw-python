# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import Parser


class ParserTestCase(TestCase):

    def setUp(self):
        self.construct_parser()
        self.addCleanup(self.wipe_parser)

    def wipe_parser(self):
        del self.parser

    def construct_parser(self):
        self.parser = Parser()


class ConstructorUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)


class AddSubparsersUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)


class AttachBelowUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)


class AttachUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)


class PrintHelpBelowUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)


class PrintHelpUnitTests(ParserTestCase):

    def setUp(self):
        ParserTestCase.setUp(self)
