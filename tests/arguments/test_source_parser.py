# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import SourceParser


class SourceParserTestCase(TestCase):

    def setUp(self):
        self.construct_source_parser()
        self.addCleanup(self.wipe_source_parser)

    def wipe_source_parser(self):
        del self.source_parser

    def construct_source_parser(self):
        self.source_parser = SourceParser()


class ConstructorUnitTests(SourceParserTestCase):

    def setUp(self):
        SourceParserTestCase.setUp(self)


class AddParserUnitTests(SourceParserTestCase):

    def setUp(self):
        SourceParserTestCase.setUp(self)


class ParseArgsUnitTests(SourceParserTestCase):

    def setUp(self):
        SourceParserTestCase.setUp(self)
