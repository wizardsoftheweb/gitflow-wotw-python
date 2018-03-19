``gitflow-wotw``
~~~~~~~~~~~~~~~~

.. image:: https://badge.fury.io/py/gitflow-wotw.svg
    :target: https://badge.fury.io/py/gitflow-wotw

.. image:: https://travis-ci.org/wizardsoftheweb/gitflow-wotw.svg?branch=master
    :target: https://travis-ci.org/wizardsoftheweb/gitflow-wotw

.. image:: https://coveralls.io/repos/github/wizardsoftheweb/gitflow-wotw/badge.svg?branch=master
    :target: https://coveralls.io/github/wizardsoftheweb/gitflow-wotw?branch=master

``gitflow-wotw`` has grand aspirations to be ``gitflow-avh`` in Python.

Please note that this is not yet stable. I've refactored massively twice now. Luckily that's not a huge issue because the code didn't do anything before.

.. contents::

Suggested Reading
=================

* The original `git flow article <http://nvie.com/posts/a-successful-git-branching-model/>`_
* |gitflow|_ (seriously outdated)
* |gitflow_avh|_ (highly recommended)
* `semantic versioning <https://semver.org>`_ (it makes so much sense)

.. |gitflow| replace:: The first ``gitflow`` implementation
.. _gitflow: https://github.com/nvie/gitflow
.. |gitflow_avh| replace:: An updated and active fork, ``gitflow-avh``
.. _gitflow_avh: https://github.com/petervanderdoes/gitflow-avh

Installation
============

.. code:: shell-session

    $ pip install --user gitflow-wotw

Usage
=====

.. code:: shell-session

    $ export PATH=~/.local/bin:$PATH
    $ which git-wotw
    ~/.local/bin/git-wotw
    $ git wotw
    < should print the main help >

Logging
=======

Log levels come from |main_verboselogs|_. It's useful to have a few extra channels. There shouldn't be any conflicts as this (theoretically) runs entirely in the console.

.. |main_verboselogs| replace:: the excellent ``verboselogs`` package
.. _main_verboselogs: https://pypi.python.org/pypi/verboselogs

Levels
------

More information can be found in |verboselogs_levels|_.

* ``SPAM``: ``-vvvvv``
* ``DEBUG``: ``-vvvv``
* ``VERBOSE``: ``-vvv``
* ``INFO``: ``-vv``
* ``NOTICE``: ``-v``
* ``WARNING``: default
* ``SUCCESS``: ``-q``
* ``ERROR``: ``-qq``
* ``CRITICAL``: ``-qqq``

.. |verboselogs_levels| replace:: the official ``verboselogs`` docs
.. _verboselogs_levels: https://pypi.python.org/pypi/verboselogs#overview-of-logging-levels

Changing the Level
------------------

To increase the level, use more ``v``'s.

.. code:: shell-session

    $ git wotw -vvvvv

To decrease the level, use more ``q``'s.

.. code:: shell-session

    $ git wotw -qqq

Roadmap
=======

These percentages are pretty arbitrary. Today's 47% could be tomorrow's 90% or vice versa.

Main Features
-------------

Once all of these are finished, I'll release ``v1``. Until then, ``v0`` should be used with caution, because it's not stable.

.. csv-table::
    :header: "Progress", "Feature"

    "0%", "``init`` support"
    "0%", "``feature`` support"
    "0%", "``bugfix`` support"
    "0%", "``release`` support"
    "0%", "``hotfix`` support"
    "0%", "``support`` support"
    "0%", "``version`` support"
    "0%", "``config`` support"
    "0%", "``log`` support"
    "0%", "Negatable options"
    "50%", "Add opt-out for ``no-`` booleans"
    "0%", "Convert ``-v`` to a count"
    "0%", "Prune extra delete options"
    "0%", "Add more ``git`` messaging"

Eventual Features
-----------------

These are things I'd like to add, but might not be included in ``v1``. If not, they'll most likely constitute one or more minor version increments.

.. csv-table::
    :header: "Progress", "Feature"

    "0%", "Repo reflection"
    "0%", "``pygit2`` alternatives"
    "0%", "semver bindings"
    "0%", "Replace ``git wotw`` with ``git flow``"
    "0%", "Local hooks connected to ``gitflow`` actions"
    "0%", "User-defined shortcuts"
    "0%", "Create ``arguments`` from config files"
    "0%", "Create ``actions`` from config files"
    "0%", "Create ``subcommands`` from config files"
    "0%", "Create the main ``command`` from config files"
    "0%", "Shell completion (bolster existing ``gitflow`` completion)"
    "0%", "``subcommand``-detecting ``action``s, e.g. ``git wotw finish release/1.0.0`` finishes a release branch"
    "0%", "``subcommand``-agnostic ``action``s, e.g. ``git wotw publish some-cool-feature`` publishes a feature branch"

Far Future Features
-------------------

.. csv-table::
    :header: "Progress", "Feature"

    "0%", "Make ``pygit2`` play well enough with everyone else to actually use"

Aside
=====

I started the current refactor (``>=0.6.0``) to speed things up. My first attempt starting taking a few seconds to render the help menu because it initialized everything before running anything. I've rewritten things to be generated on the fly. However, once again, everything has be generated on the fly before anything can run (To create the root, I have to create its dependencies. But to create its dependencies, I have to create their dependencies. And so on.) I think this direction is a little smarter but it will probably involve less cool reflection and more boilerplate.

As of ``>=0.7.0``, I've got some delayed callbacks in place to keep things speedy. Previously, everything was getting created in ``ObjectBuilder`` on launch. Now ``Action``s are built with a factory in ``process``, which means the necessary ``Command`` won't get loaded until the ``Action`` has fired. It keeps things much slimmer.
