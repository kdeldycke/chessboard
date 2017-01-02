Usage
=====


``chessboard``
--------------

List global options and commands:

.. code-block:: shell-session

    $ chessboard --help
    Usage: chessboard [OPTIONS] COMMAND [ARGS]...

      CLI to solve combinatoric chess puzzles.

    Options:
      --version      Show the version and exit.
      -v, --verbose  Print much more debug statements.
      --help         Show this message and exit.

    Commands:
      benchmark  Benchmark the solver.
      graph      Plot solver performances.
      solve      Solve a chess puzzle.


``chessboard solve``
--------------------

Solver specific options:

.. code-block:: shell-session

    $ chessboard solve --help
    Usage: chessboard solve [OPTIONS]

      Solve a puzzle constrained by board dimensions and pieces.

    Options:
      -l, --length INTEGER  Length of the board.  [required]
      -h, --height INTEGER  Height of the board.  [required]
      -s, --silent          Do not render result boards in ASCII-art.
      -p, --profile         Produce a profiling graph.
      --queen INTEGER       Number of queens.
      --king INTEGER        Number of kings.
      --rook INTEGER        Number of rooks.
      --bishop INTEGER      Number of bishops.
      --knight INTEGER      Number of knights.
      --help                Show this message and exit.


``chessboard benchmark``
------------------------

Benchmark specific options:

.. code-block:: shell-session

    $ chessboard benchmark --help
    Usage: chessboard benchmark [OPTIONS]

      Run a benchmarking suite and measure time taken by the solver.

      Each scenario is run in an isolated process, and results are appended to
      CSV file.

    Options:
      --help  Show this message and exit.


``chessboard plot``
-------------------

Plotting specific options:

.. code-block:: shell-session

    $ chessboard plot --help
    Usage: chessboard graph [OPTIONS]

      Update all kind of performance graphs from the benchmark data.

      All data come from CSV database.

    Options:
      --help  Show this message and exit.
