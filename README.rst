Chessboard
==========

Python CLI to explore chessboard positions.

Stable release: |release| |dependencies| |license| |popularity|

Development: |build| |coverage| |quality|

.. |release| image:: https://img.shields.io/pypi/v/chessboard.svg?style=flat
    :target: https://pypi.python.org/pypi/chessboard
    :alt: Last release
.. |license| image:: https://img.shields.io/pypi/l/chessboard.svg?style=flat
    :target: https://www.gnu.org/licenses/gpl-2.0.html
    :alt: Software license
.. |popularity| image:: https://img.shields.io/pypi/dm/chessboard.svg?style=flat
    :target: https://pypi.python.org/pypi/chessboard#downloads
    :alt: Popularity
.. |dependencies| image:: https://img.shields.io/requires/github/kdeldycke/chessboard/master.svg?style=flat
    :target: https://requires.io/github/kdeldycke/chessboard/requirements/?branch=master
    :alt: Requirements freshness
.. |build| image:: https://img.shields.io/travis/kdeldycke/chessboard/develop.svg?style=flat
    :target: https://travis-ci.org/kdeldycke/chessboard
    :alt: Unit-tests status
.. |coverage| image:: https://coveralls.io/repos/kdeldycke/chessboard/badge.svg?branch=develop&service=github
    :target: https://coveralls.io/r/kdeldycke/chessboard?branch=develop
    :alt: Coverage Status
.. |quality| image:: https://img.shields.io/scrutinizer/g/kdeldycke/chessboard.svg?style=flat
    :target: https://scrutinizer-ci.com/g/kdeldycke/chessboard/?branch=develop
    :alt: Code Quality


Motivation
----------

This project is a playground to test some optimization strategies in Python,
but is essentially an exemple of a real-life Python package, and serve me as
a boilerplate project for future CLI.


Development philosophy
----------------------

1. First create something that work (to provide business value).
2. Then something that's beautiful (to lower maintenance costs).
3. Finally works on performance (to avoid wasting time on premature
   optimizations).


Install
-------

This package is available on PyPi, so you can install the latest stable release
and its dependencies with a simple `pip` call:

.. code-block:: bash

    $ pip install chessboard


Usage
-----

.. code-block:: bash

    $ chessboard --help
    Usage: chessboard [OPTIONS]

      Python CLI to explore chessboard positions.

    Options:
      --version             Show the version and exit.
      -l, --length INTEGER  Length of the board.  [required]
      -h, --height INTEGER  Height of the board.  [required]
      -s, --silent          Do not display result board, only final count.
      -v, --verbose         Print much more debug statements.
      -p, --profile         Produce a profiling graph.
      --rook INTEGER        Number of rooks to add to the board.
      --knight INTEGER      Number of knights to add to the board.
      --queen INTEGER       Number of queens to add to the board.
      --bishop INTEGER      Number of bishops to add to the board.
      --king INTEGER        Number of kings to add to the board.
      --help                Show this message and exit.


Examples
--------

Simple 3x3 board with 2 kings and a rook:

.. code-block:: bash

    $ chessboard --length=3 --height=3 --king=2 --rook=1
    <SolverContext: length=3, height=3, pieces={'rook': 1, 'king': 2, 'queen': 0, 'bishop': 0, 'knight': 0}>
    Searching positions...
    ┌───┬───┬───┐
    │ ♚ │   │   │
    ├───┼───┼───┤
    │   │   │ ♜ │
    ├───┼───┼───┤
    │ ♚ │   │   │
    └───┴───┴───┘
    ┌───┬───┬───┐
    │   │   │ ♚ │
    ├───┼───┼───┤
    │ ♜ │   │   │
    ├───┼───┼───┤
    │   │   │ ♚ │
    └───┴───┴───┘
    ┌───┬───┬───┐
    │ ♚ │   │ ♚ │
    ├───┼───┼───┤
    │   │   │   │
    ├───┼───┼───┤
    │   │ ♜ │   │
    └───┴───┴───┘
    ┌───┬───┬───┐
    │   │ ♜ │   │
    ├───┼───┼───┤
    │   │   │   │
    ├───┼───┼───┤
    │ ♚ │   │ ♚ │
    └───┴───┴───┘
    4 results found in 0.03 seconds.


Famous eight queens puzzle:

.. code-block:: bash

    $ chessboard --length=8 --height=8 --queen=8 --silent
    <SolverContext: length=8, height=8, pieces={'rook': 0, 'king': 0, 'queen': 8, 'bishop': 0, 'knight': 0}>
    Searching positions...
    92 results found in 119.87 seconds.


Huge combinatoric problem:

.. code-block:: bash

    $ chessboard --length=7 --height=7 --king=2 --queen=2 --bishop=2 --knight=1 --silent
    <SolverContext: length=7, height=7, pieces={'rook': 0, 'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1}>
    Searching positions...
    3063828 results found in 93614.93 seconds.


Performances
------------

Results below were run with the ``--silent`` option.

+--------------------+------+-----------+--------------+--------------+
| Pieces             | Size | Solutions | MacBook      | C1 instance  |
|                    |      |           | Air 5,2 [#]_ | [#]_         |
+====================+======+===========+==============+==============+
| 2 kings, 1 rook    |  3x3 |         4 |      0.01 s. |           ?  |
+--------------------+------+-----------+--------------+--------------+
| 2 rooks, 4 knights |  4x4 |         8 |      0.15 s. |      1.06 s. |
+--------------------+------+-----------+--------------+--------------+
| 1 queen            |  1x1 |         1 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 2 queens           |  2x2 |         0 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 3 queens           |  3x3 |         0 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 4 queens           |  4x4 |         2 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 5 queens           |  5x5 |        10 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 6 queens           |  6x6 |         4 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 7 queens           |  7x7 |        40 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 8 queens           |  8x8 |        92 |     94.05 s. |    742.09 s. |
+--------------------+------+-----------+--------------+--------------+
| 9 queens           |  9x9 |       352 |           s. |           s. |
+--------------------+------+-----------+--------------+--------------+
| 2 kings,           |  5x5 |         8 |      3.79 s. |     27.42 s. |
| 2 queens,          +------+-----------+--------------+--------------+
| 2 bishops,         |  6x6 |    23 752 |    228.36 s. |  1 754.60 s. |
| 1 knight           +------+-----------+--------------+--------------+
|                    |  7x7 | 3 063 828 |           s. | 93 614.93 s. |
+--------------------+------+-----------+--------------+--------------+

Results from the table above came from running the ``benchmark.sh`` script in a
detached background process:

.. code-block:: bash

    $ nohup ./benchmark.sh > benchmark.out 2> benchmark.err < /dev/null &
    $ tail -F benchmark.out

All tests are run with the ``--silent`` option.

.. [#] MacBook Air 5,2; x86 64 bits, 2.0 GHz 2-cores i7-3667U CPU; 8 GB,
       1600 MHz DDR3 RAM; SSD Flash storage; OSX Yosemite 10.10.5;
       Python 2.7.10.

.. [#] `Scaleway C1 compute instance <https://scaleway.com>`_; ARMv7 32 bits,
       4-cores Marvell Cortex A9 Armada 370/XP CPU; 2 GB RAM; SSD Flash
       storage; Ubuntu Vivid 15.04; Python 2.7.9.


Development
-----------

Check out latest development branch:

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ cd ./chessboard
    $ python ./setup.py develop

Run unit-tests:

.. code-block:: bash

    $ python ./setup.py nosetests


Stability policy
----------------

Here is a bunch of rules we're trying to follow regarding stability:

* Patch releases (``0.x.n`` → ``0.x.(n+1)`` upgrades) are bug-fix only. These
  releases must not break anything and keeps backward-compatibility with
  ``0.x.*`` and ``0.(x-1).*`` series.

* Minor releases (``0.n.*`` → ``0.(n+1).0`` upgrades) includes any non-bugfix
  changes. These releases must be backward-compatible with any ``0.n.*``
  version but are allowed to drop compatibility with the ``0.(n-1).*`` series
  and below.

* Major releases (``n.*.*`` → ``(n+1).0.0`` upgrades) are not planned yet:
  we're still in beta and the final feature set of the ``1.0.0`` release is not
  decided yet.


Release process
---------------

Start from the ``develop`` branch:

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ git checkout develop

Revision should already be set to the next version, so we just need to set the
released date in the changelog:

.. code-block:: bash

    $ vi ./CHANGES.rst

Create a release commit, tag it and merge it back to ``master`` branch:

.. code-block:: bash

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

.. code-block:: bash

    $ pip install wheel
    $ python ./setup.py register -r testpypi
    $ rm -rf ./build ./dist
    $ python ./setup.py sdist bdist_egg bdist_wheel upload -r testpypi

Publish packaging to `PyPi <https://pypi.python.org>`_:

.. code-block:: bash

    $ python ./setup.py register -r pypi
    $ rm -rf ./build ./dist
    $ python ./setup.py sdist bdist_egg bdist_wheel upload -r pypi

Bump revision back to its development state:

.. code-block:: bash

    $ pip install bumpversion
    $ git checkout develop
    $ bumpversion --verbose patch
    $ git add ./chessboard/__init__.py ./CHANGES.rst
    $ git commit -m "Post release version bump."
    $ git push

Now if the next revision is no longer bug-fix only:

.. code-block:: bash

    $ bumpversion --verbose minor
    $ git add ./chessboard/__init__.py ./CHANGES.rst
    $ git commit -m "Next release no longer bug-fix only. Bump revision."
    $ git push


Third-party
-----------

This project package's boilerplate is sourced from the `code I wrote
<https://github.com/scaleway/postal-address/graphs/contributors>`_ for
`Scaleway <https://scaleway.com/>`_'s `postal-address module
<https://github.com/scaleway/postal-address>`_, which is published under a
`GPLv2+ License <https://github.com/scaleway/postal-address#license>`_.

The CLI code is based on the one I wrote for the `kdenlive-tools module
<https://github.com/kdeldycke/kdenlive-tools>`_, published under a `BSD
license <https://github.com/kdeldycke/kdenlive-tools/blob/master/LICENSE>`_.


License
-------

This software is licensed under the `GNU General Public License v2 or later
(GPLv2+)
<https://github.com/kdeldycke/chessboard/blob/master/LICENSE>`_.
