ChangeLog
=========


0.9.0 (unreleased)
------------------

* No changes yet.


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
