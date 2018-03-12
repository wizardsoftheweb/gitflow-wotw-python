# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import ParserSource


class ParserSourceTestCase(TestCase):

    def setUp(self):
        self.construct_parser_source()
        self.addCleanup(self.wipe_parser_source)

    def wipe_parser_source(self):
        del self.parser_source

    def construct_parser_source(self):
        self.parser_source = ParserSource()


class ConstructorUnitTests(ParserSourceTestCase):

    def setUp(self):
        ParserSourceTestCase.setUp(self)


class AddParserUnitTests(ParserSourceTestCase):

    def setUp(self):
        ParserSourceTestCase.setUp(self)


class ParseArgsUnitTests(ParserSourceTestCase):

    def setUp(self):
        ParserSourceTestCase.setUp(self)
