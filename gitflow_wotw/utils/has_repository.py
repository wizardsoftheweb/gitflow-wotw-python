# pylint:disable=W,C,R

from __future__ import print_function

from os import getcwd
from os.path import abspath, expanduser, expandvars, normpath, relpath

# pylint: disable=no-name-in-module
from pygit2 import discover_repository
# pylint: enable=no-name-in-module
from pygit2 import Repository


class HasRepository(object):

    def __init__(self, directory=None):
        self.update_repo_path(directory)

    def update_repo_path(self, directory=None):
        if directory is None:
            directory = getcwd()
        else:
            directory = self.resolve_absolute_path(directory)
        repo_path = discover_repository(directory)
        self.repo = Repository(repo_path)

    @staticmethod
    def resolve_absolute_path(path_to_resolve):
        return abspath(
            relpath(
                expandvars(
                    expanduser(
                        path_to_resolve
                    )
                )
            )
        )
