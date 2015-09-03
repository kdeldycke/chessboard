ChangeLog
=========


1.2.0 (2015-09-03)
------------------

* Pre-compute some Board properties. Add 1.12x speedup.
* Reuse Board object. Add 1.06x speedup.
* Use list of boolean instead of bytearray for states in Board. Add 1.11x
  speedup.
* Add a little benchmark suite.


1.1.0 (2015-08-28)
------------------

* Use `bytearray` to represent board states. Closes #4.
* Cache piece territories to speed solver up to 3x on board with big population
  of pieces.


1.0.0 (2015-08-27)
------------------

* Do not spend time converting back and forth linear position to 2D position.
  Provides a 1.16x speed-up.
* Proceed permutation exploration with pieces of biggest territory coverage
  first. Adds 16x speed-up. Closes #5.
* Add support for bumpversion.
* Add new ``--profile`` option to produce an execution profile of the solver.


0.9.1 (2015-08-25)
------------------

* Fix rendering of unicode string in terminal.
* Document stability policy and release process.
* Add PyPi-based badges.


0.9.0 (2015-08-25)
------------------

* Validate CLI user inputs and provides hints.
* Abandon branches of the search space as soon as possible. Closes #3.
* Deduplicate per-kind piece group permutations early. Closes #7.
* Add ``--silent`` option to skip displaying of all board results in ASCII art.


0.8.0 (2015-08-15)
------------------

* Refactor solver to deduplicate positions by kind (combination) before
  iterating the search space by brute force (cartesian product).


0.7.0 (2015-08-14)
------------------

* Display results in unicode-art.


0.6.0 (2015-08-14)
------------------

* Add Knight model.


0.5.0 (2015-08-13)
------------------

* Add Rook and Bishop models.
* Allow overlapping but non-threatening territory of pieces to co-exists.


0.4.0 (2015-08-13)
------------------

* Add project status badges.
* Enable continuous integration metrics: build status, coverage and code
  quality.
* Fix index to position computation in non-square boards.
* Remove restriction on board dimensions.
* Unit-tests result sets produced by the solver.


0.3.0 (2015-08-12)
------------------

* Add Queen piece.
* Fix displaying of piece representation.
* Fix persistence of square occupancy between each piece addition.


0.2.1 (2015-08-11)
------------------

* Fix King displacement map.


0.2.0 (2015-08-11)
------------------

* Allow initialization of board pieces.
* Implement brute-force solver.


0.1.1 (2015-08-08)
------------------

* Package re-release to fix bad version number.


0.1.0 (2015-08-08)
------------------

* First public release.
* Implements a CLI to inititalize the chessboard.


0.0.0 (2015-08-08)
------------------

* First commit.
