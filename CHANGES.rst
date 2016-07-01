ChangeLog
=========


`1.5.0 (2016-07-01) <http://github.com/kdeldycke/chessboard/compare/v1.4.0...v1.5.0>`_
--------------------------------------------------------------------------------------

.. note:: This version is not yet released and is under active development.

* Add default ``isort`` configuration.
* Add more trove classifiers.
* Add proper support of logging. Closes #2.
* Use Miniconda to install ``numpy``, ``scipy``, ``matplotlib`` and ``pandas``
  in Travis builds.
* Activate unittests in Python 3.3, 3.4 and 3.5. Closes #9.
* Activate unittests on OSX.
* Get detailed CPU info for each benckmark.
* Add sphinx-based documentation.
* Use ``pip`` to install package and other extra dependencies.
* Add a git mailmap template.


`1.4.0 (2015-11-23) <http://github.com/kdeldycke/chessboard/compare/v1.3.0...v1.4.0>`_
--------------------------------------------------------------------------------------

* Make the solver into a CLI sub-command.
* Pythonize benchmarking and include it as a CLI sub-command.
* Plot n-queens graph from benchmark data.
* Switch from coveralls.io to codecov.io.


`1.3.0 (2015-09-06) <http://github.com/kdeldycke/chessboard/compare/v1.2.0...v1.3.0>`_
--------------------------------------------------------------------------------------

* Only compute 2D coordinates of each piece instance when needed, so we can
  reach immediately the cache if we're only interested by the territory. Adds
  a 1.21x speedup.
* Add custom PEP8 configuration.
* Add custom Pylint configuration.


`1.2.0 (2015-09-03) <http://github.com/kdeldycke/chessboard/compare/v1.1.0...v1.2.0>`_
--------------------------------------------------------------------------------------

* Pre-compute some Board properties. Adds a 1.12x speedup.
* Reuse Board object. Adds a 1.06x speedup.
* Use list of boolean instead of bytearray for states in Board. Adds a 1.11x
  speedup.
* Add a little benchmark suite.


`1.1.0 (2015-08-28) <http://github.com/kdeldycke/chessboard/compare/v1.0.0...v1.1.0>`_
--------------------------------------------------------------------------------------

* Use `bytearray` to represent board states. Closes #4.
* Cache piece territories to speed solver up to 3x on board with big population
  of pieces.


`1.0.0 (2015-08-27) <http://github.com/kdeldycke/chessboard/compare/v0.9.1...v1.0.0>`_
--------------------------------------------------------------------------------------

* Do not spend time converting back and forth linear position to 2D position.
  Provides a 1.16x speedup.
* Proceed permutation exploration with pieces of biggest territory coverage
  first. Adds 16x speed-up. Closes #5.
* Add support for bumpversion.
* Add new ``--profile`` option to produce an execution profile of the solver.


`0.9.1 (2015-08-25) <http://github.com/kdeldycke/chessboard/compare/v0.9.0...v0.9.1>`_
--------------------------------------------------------------------------------------

* Fix rendering of unicode string in terminal.
* Document stability policy and release process.
* Add PyPi-based badges.


`0.9.0 (2015-08-25) <http://github.com/kdeldycke/chessboard/compare/v0.8.0...v0.9.0>`_
--------------------------------------------------------------------------------------

* Validate CLI user inputs and provides hints.
* Abandon branches of the search space as soon as possible. Closes #3.
* Deduplicate per-kind piece group permutations early. Closes #7.
* Add ``--silent`` option to skip displaying of all board results in ASCII art.


`0.8.0 (2015-08-15) <http://github.com/kdeldycke/chessboard/compare/v0.7.0...v0.8.0>`_
--------------------------------------------------------------------------------------

* Refactor solver to deduplicate positions by kind (combination) before
  iterating the search space by brute force (cartesian product).


`0.7.0 (2015-08-14) <http://github.com/kdeldycke/chessboard/compare/v0.6.0...v0.7.0>`_
--------------------------------------------------------------------------------------

* Display results in unicode-art.


`0.6.0 (2015-08-14) <http://github.com/kdeldycke/chessboard/compare/v0.5.0...v0.6.0>`_
--------------------------------------------------------------------------------------

* Add Knight model.


`0.5.0 (2015-08-13) <http://github.com/kdeldycke/chessboard/compare/v0.4.0...v0.5.0>`_
--------------------------------------------------------------------------------------

* Add Rook and Bishop models.
* Allow overlapping but non-threatening territory of pieces to co-exists.


`0.4.0 (2015-08-13) <http://github.com/kdeldycke/chessboard/compare/v0.3.0...v0.4.0>`_
--------------------------------------------------------------------------------------

* Add project status badges.
* Enable continuous integration metrics: build status, coverage and code
  quality.
* Fix index to position computation in non-square boards.
* Remove restriction on board dimensions.
* Unit-tests result sets produced by the solver.


`0.3.0 (2015-08-12) <http://github.com/kdeldycke/chessboard/compare/v0.2.1...v0.3.0>`_
--------------------------------------------------------------------------------------

* Add Queen piece.
* Fix displaying of piece representation.
* Fix persistence of square occupancy between each piece addition.


`0.2.1 (2015-08-11) <http://github.com/kdeldycke/chessboard/compare/v0.2.0...v0.2.1>`_
--------------------------------------------------------------------------------------

* Fix King displacement map.


`0.2.0 (2015-08-11) <http://github.com/kdeldycke/chessboard/compare/v0.1.1...v0.2.0>`_
--------------------------------------------------------------------------------------

* Allow initialization of board pieces.
* Implement brute-force solver.


`0.1.1 (2015-08-08) <http://github.com/kdeldycke/chessboard/compare/v0.1.0...v0.1.1>`_
--------------------------------------------------------------------------------------

* Package re-release to fix bad version number.


`0.1.0 (2015-08-08) <http://github.com/kdeldycke/chessboard/compare/v0.0.0...v0.1.0>`_
--------------------------------------------------------------------------------------

* First public release.
* Implements a CLI to inititalize the chessboard.


`0.0.0 (2015-08-08) <https://github.com/kdeldycke/chessboard/commit/84f7d6>`_
-----------------------------------------------------------------------------

* First commit.
