Development
===========


Philosophy
----------

1. First create something that work (to provide business value).
2. Then something that's beautiful (to lower maintenance costs).
3. Finally works on performance (to avoid wasting time on premature
   optimizations).


Stability policy
----------------

This project follows `Semantic Versioning <https://semver.org/>`_.

Which boils down to the following rules of thumb regarding stability:

* **Patch releases** (``0.x.n`` → ``0.x.(n+1)`` upgrades) are bug-fix only.
  These releases must not break anything and keeps backward-compatibility with
  ``0.x.*`` and ``0.(x-1).*`` series.

* **Minor releases** (``0.n.*`` → ``0.(n+1).0`` upgrades) includes any
  non-bugfix changes. These releases must be backward-compatible with any
  ``0.n.*`` version but are allowed to drop compatibility with the
  ``0.(n-1).*`` series and below.

* **Major releases** (``n.*.*`` → ``(n+1).0.0`` upgrades) are not planned yet,
  unless we introduce huge changes to the project.


Build status
------------

==========================  ===================  ===================
Branch                      |master-branch|__    |develop-branch|__
==========================  ===================  ===================
Unittests (macOS & Linux)   |build-stable|       |build-dev|
Unittests (Windows)         |build-stable-win|   |build-dev-win|
Coverage                    |coverage-stable|    |coverage-dev|
Quality                     |quality-stable|     |quality-dev|
Dependencies                |deps-stable|        |deps-dev|
Documentation               |docs-stable|        |docs-dev|
==========================  ===================  ===================

.. |master-branch| replace::
   ``master``
__ https://github.com/kdeldycke/chessboard/tree/master
.. |develop-branch| replace::
   ``develop``
__ https://github.com/kdeldycke/chessboard/tree/develop

.. |build-stable| image:: https://travis-ci.org/kdeldycke/chessboard.svg?branch=master
    :target: https://travis-ci.org/kdeldycke/chessboard
    :alt: Unit-tests macOS & Linux status
.. |build-dev| image:: https://travis-ci.org/kdeldycke/chessboard.svg?branch=develop
    :target: https://travis-ci.org/kdeldycke/chessboard
    :alt: Unit-tests macOS & Linux status

.. |build-stable-win| image:: https://ci.appveyor.com/api/projects/status/github/kdeldycke/chessboard?branch=master&svg=true
    :target: https://ci.appveyor.com/project/kdeldycke/chessboard
    :alt: Unit-tests Windows status
.. |build-dev-win| image:: https://ci.appveyor.com/api/projects/status/github/kdeldycke/chessboard?branch=develop&svg=true
    :target: https://ci.appveyor.com/project/kdeldycke/chessboard
    :alt: Unit-tests Windows status

.. |coverage-stable| image:: https://codecov.io/gh/kdeldycke/chessboard/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/kdeldycke/chessboard/branch/master
    :alt: Coverage Status
.. |coverage-dev| image:: https://codecov.io/gh/kdeldycke/chessboard/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/kdeldycke/chessboard/branch/develop
    :alt: Coverage Status

.. |quality-stable| image:: https://scrutinizer-ci.com/g/kdeldycke/chessboard/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/kdeldycke/chessboard/?branch=master
    :alt: Code Quality
.. |quality-dev| image:: https://scrutinizer-ci.com/g/kdeldycke/chessboard/badges/quality-score.png?b=develop
    :target: https://scrutinizer-ci.com/g/kdeldycke/chessboard/?branch=develop
    :alt: Code Quality

.. |deps-stable| image:: https://requires.io/github/kdeldycke/chessboard/requirements.svg?branch=master
    :target: https://requires.io/github/kdeldycke/chessboard/requirements/?branch=master
    :alt: Requirements freshness
.. |deps-dev| image:: https://requires.io/github/kdeldycke/chessboard/requirements.svg?branch=develop
    :target: https://requires.io/github/kdeldycke/chessboard/requirements/?branch=develop
    :alt: Requirements freshness

.. |docs-stable| image:: https://readthedocs.org/projects/chessboard/badge/?version=stable
    :target: https://chessboard.readthedocs.io/en/stable/
    :alt: Documentation Status
.. |docs-dev| image:: https://readthedocs.org/projects/chessboard/badge/?version=develop
    :target: https://chessboard.readthedocs.io/en/develop/
    :alt: Documentation Status


Setup a development environment
-------------------------------

Check out latest development branch:

.. code-block:: shell-session

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ cd ./chessboard
    $ git checkout develop

Install package in editable mode with all development dependencies:

.. code-block:: shell-session

    $ pip install -e .[develop]

Now you're ready to hack and abuse git!


Unit-tests
----------

Install test dependencies and run unit-tests:

.. code-block:: shell-session

    $ pip install -e .[tests]
    $ pytest


Dependencies
------------

Because `pip doesn't have true dependency resolution yet
<https://github.com/pypa/pip/issues/988>`_ we need to check we do not have any
conflicting dependencies:

.. code-block:: shell-session

    $ pip install -e .[tests]
    $ pipdeptree

And once in a while, it's good to upgrade the graph of package dependencies:

.. code-block:: shell-session

    $ pipdeptree --packages chessboard --graph-output png > ./docs/dependencies.png


Coding style
------------

Run `isort <https://github.com/timothycrosley/isort>`_ utility to sort Python
imports:

.. code-block:: shell-session

    $ pip install -e .[develop]
    $ isort --apply

Then run `pycodestyle <https://pycodestyle.readthedocs.io>`_ and `Pylint
<https://docs.pylint.org>`_ code style checks:

.. code-block:: shell-session

    $ pip install -e .[tests]
    $ pycodestyle chessboard
    $ pylint --rcfile=setup.cfg chessboard


Build documentation
-------------------

The documentation you're currently reading can be built locally with `Sphinx
<https://www.sphinx-doc.org>`_:

.. code-block:: shell-session

    $ pip install -e .[docs]
    $ sphinx-apidoc -f -o ./docs .
    $ sphinx-build -b html ./docs ./docs/html

For a smooth release, you also need to validate the rendering of package's long
description on PyPi, as well as metadata:

.. code-block:: shell-session

    $ pip install -e .[develop]
    $ ./setup.py check -m -r -s


Release process
---------------

Start from the ``develop`` branch:

.. code-block:: shell-session

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ cd ./chessboard
    $ git checkout develop

Install development dependencies:

.. code-block:: shell-session

    $ pip install -e .[develop]

Revision should already be set to the next version, so we just need to set the
released date in the changelog:

.. code-block:: shell-session

    $ vi ./CHANGES.rst

Create a release commit, tag it and merge it back to ``master`` branch:

.. code-block:: shell-session

    $ git add ./chessboard/__init__.py ./CHANGES.rst
    $ git commit -m "Release vX.Y.Z"
    $ git tag "vX.Y.Z"
    $ git push
    $ git push --tags
    $ git checkout master
    $ git pull
    $ git merge "vX.Y.Z"
    $ git push

Push packaging to the `test cheeseshop
<https://wiki.python.org/moin/TestPyPI>`_:

.. code-block:: shell-session

    $ ./setup.py clean --all
    $ ./setup.py sdist bdist_egg bdist_wheel
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Publish package to `PyPi <https://pypi.python.org>`_:

.. code-block:: shell-session

    $ ./setup.py clean --all
    $ ./setup.py sdist bdist_egg bdist_wheel
    $ twine upload dist/*

Update revision with `bumpversion <https://github.com/peritus/bumpversion>`_
and set it back to development state by increasing the ``patch`` level.

.. code-block:: shell-session

    $ git checkout develop
    $ bumpversion --verbose patch
    $ git add ./chessboard/__init__.py ./CHANGES.rst
    $ git commit -m "Post release version bump."
    $ git push

Now if the next revision is no longer bug-fix only, bump the ``minor``
revision level instead:

.. code-block:: shell-session

    $ bumpversion --verbose minor
    $ git add ./chessboard/__init__.py ./CHANGES.rst
    $ git commit -m "Next release no longer bug-fix only. Bump revision."
    $ git push
