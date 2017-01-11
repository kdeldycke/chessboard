Chessboard
==========

CLI to solve combinatoric chess puzzles.

Stable release: |release| |versions| |license| |dependencies|

Development: |build| |docs| |coverage| |quality|

.. |release| image:: https://img.shields.io/pypi/v/chessboard.svg
    :target: https://pypi.python.org/pypi/chessboard
    :alt: Last release
.. |versions| image:: https://img.shields.io/pypi/pyversions/chessboard.svg
    :target: https://pypi.python.org/pypi/chessboard
    :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/chessboard.svg
    :target: https://www.gnu.org/licenses/gpl-2.0.html
    :alt: Software license
.. |dependencies| image:: https://requires.io/github/kdeldycke/chessboard/requirements.svg?branch=master
    :target: https://requires.io/github/kdeldycke/chessboard/requirements/?branch=master
    :alt: Requirements freshness
.. |build| image:: https://travis-ci.org/kdeldycke/chessboard.svg?branch=develop
    :target: https://travis-ci.org/kdeldycke/chessboard
    :alt: Unit-tests status
.. |docs| image:: https://readthedocs.org/projects/chessboard/badge/?version=develop
    :target: https://chessboard.readthedocs.io/en/develop/
    :alt: Documentation Status
.. |coverage| image:: https://codecov.io/gh/kdeldycke/chessboard/branch/develop/graph/badge.svg
    :target: https://codecov.io/github/kdeldycke/chessboard?branch=develop
    :alt: Coverage Status
.. |quality| image:: https://scrutinizer-ci.com/g/kdeldycke/chessboard/badges/quality-score.png?b=develop
    :target: https://scrutinizer-ci.com/g/kdeldycke/chessboard/?branch=develop
    :alt: Code Quality


Motivation
----------

This project started its life as a coding challenge I was asked to solve while
interviewing in 2015 for a software engineering position at
`Uber <https://www.uber.com/careers/>`_.

After the interview proccess ended, I kept toying with the code, as a playground
to test some optimization strategies in Python. It is now a boilerplate that
I use to:

* bootstrap CLI-based projects powered with `Click <https://click.pocoo.org>`_,
* keep up with the current state-of-art of `Python packaging <https://pypa.io>`_,
* streamline the integration of a data stack (`Numpy <https://numpy.org>`_,
  `Pandas <https://pandas.pydata.org>`_,
  `Seaborn <https://stanford.edu/~mwaskom/software/seaborn>`_ and
  `Conda <https://conda.anaconda.org>`_),
* automate `testing and quality checks <https://meta.pycqa.org>`_ (unit-tests,
  coverage, coding style and packaging),
* provide an `auto-generated documentation <https://chessboard.readthedocs.io>`_.


Examples
--------

Simple 3x3 board with 2 kings and a rook:

.. code-block:: shell-session

    $ chessboard solve --length=3 --height=3 --king=2 --rook=1
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

Famous eight queens puzzle, without printing the solutions to speed things up:

.. code-block:: shell-session

    $ chessboard solve --length=8 --height=8 --queen=8 --silent
    <SolverContext: length=8, height=8, pieces={'rook': 0, 'king': 0, 'queen': 8, 'bishop': 0, 'knight': 0}>
    Searching positions...
    92 results found in 119.87 seconds.

Huge combinatoric problem can take some time to solve:

.. code-block:: shell-session

    $ chessboard solve --length=7 --height=7 --king=2 --queen=2 --bishop=2 --knight=1 --silent
    <SolverContext: length=7, height=7, pieces={'rook': 0, 'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1}>
    Searching positions...
    3063828 results found in 9328.33 seconds.

The CLI allow the production of a profiling graph, to identify code hot spots and
bottleneck:.

.. code-block:: shell-session

    $ chessboard solve --length=6 --height=6 --king=2 --queen=2 --bishop=2 --knight=1 --silent --profile
    <SolverContext: length=6, height=6, pieces={'rook': 0, 'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1}>
    Searching positions...
    23752 results found in 207.25 seconds.
    Execution profile saved at /home/kevin/chessboard/solver-profile.png

.. image:: https://raw.githubusercontent.com/kdeldycke/chessboard/develop/solver-profile.png
   :alt: Solver profiling graph
   :align: center


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


Other resources
---------------

* `Awesome Chess: curated list of assets
  <https://github.com/hkirat/awesome-chess>`_
* `Combinatorial Generation <https://www.1stworks.com/ref/RuskeyCombGen.pdf>`_
* `Applied Combinatorics <https://people.math.gatech.edu/~trotter/book.pdf>`_
* `Extremal Problems <https://www-math.mit.edu/~rstan/transparencies/iap.pdf>`_
* `Combinatorial Algorithms <https://news.ycombinator.com/item?id=13306704>`_
