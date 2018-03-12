# pylint: disable=missing-docstring

from __future__ import print_function

from unittest import TestCase

from mock import call, MagicMock, patch

from gitflow_wotw import FeatureSubcommand


class FeatureSubcommandTestCase(TestCase):

    def setUp(self):
        self.construct_feature_subcommand()
        self.addCleanup(self.wipe_feature_subcommand)

    def wipe_feature_subcommand(self):
        del self.feature_subcommand

    def construct_feature_subcommand(self):
        self.feature_subcommand = FeatureSubcommand()


class ConstructorUnitTests(FeatureSubcommandTestCase):

    def setUp(self):
        FeatureSubcommandTestCase.setUp(self)


class PopulateUnitTests(FeatureSubcommandTestCase):

    def setUp(self):
        FeatureSubcommandTestCase.setUp(self)
