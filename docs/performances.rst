Performances
============

Results below are given in seconds, and were run with the ``--silent`` option.

+--------------------+------+-----------+-----------+-------------+
| Pieces             | Size | Solutions | MacBook   | C1 instance |
|                    |      |           | Air [#]_  | [#]_        |
+====================+======+===========+===========+=============+
| 2 kings, 1 rook    |  3x3 |         4 |      0.01 |        0.04 |
+--------------------+------+-----------+-----------+-------------+
| 2 rooks, 4 knights |  4x4 |         8 |      0.12 |        0.91 |
+--------------------+------+-----------+-----------+-------------+
| 1 queen            |  1x1 |         1 |         0 |           0 |
+--------------------+------+-----------+-----------+-------------+
| 2 queens           |  2x2 |         0 |         0 |           0 |
+--------------------+------+-----------+-----------+-------------+
| 3 queens           |  3x3 |         0 |         0 |        0.02 |
+--------------------+------+-----------+-----------+-------------+
| 4 queens           |  4x4 |         2 |      0.02 |        0.10 |
+--------------------+------+-----------+-----------+-------------+
| 5 queens           |  5x5 |        10 |      0.10 |        0.80 |
+--------------------+------+-----------+-----------+-------------+
| 6 queens           |  6x6 |         4 |      0.90 |        7.10 |
+--------------------+------+-----------+-----------+-------------+
| 7 queens           |  7x7 |        40 |      8.53 |       65.55 |
+--------------------+------+-----------+-----------+-------------+
| 8 queens           |  8x8 |        92 |     85.80 |      673.28 |
+--------------------+------+-----------+-----------+-------------+
| 9 queens           |  9x9 |       352 |    900.20 |    7 282.56 |
+--------------------+------+-----------+-----------+-------------+
| 2 kings,           |  5x5 |         8 |      3.29 |       23.79 |
| 2 queens,          +------+-----------+-----------+-------------+
| 2 bishops,         |  6x6 |    23 752 |    187.40 |    1 483.31 |
| 1 knight           +------+-----------+-----------+-------------+
|                    |  7x7 | 3 063 828 |  8 150.86 |   62 704.99 |
+--------------------+------+-----------+-----------+-------------+

To run the standard benchmark suite and add results to the database, run the
benchmark in a detached background process:

.. code-block:: shell-session

    $ nohup chessboard benchmark > /dev/null 2>&1 &

.. [#] MacBook Air 5,2; x86 64 bits 2.0 GHz 2-cores i7-3667U CPU; 8 GB 1600 MHz
       DDR3 RAM; SSD Flash storage; Mac OS X Yosemite 10.10.5; Python 2.7.10.

.. [#] `Scaleway C1 compute instance <https://scaleway.com>`_; ARMv7 32 bits
       4-cores Marvell Cortex A9 Armada 370/XP CPU; 2 GB RAM; SSD Flash
       storage; Ubuntu Vivid 15.04; Python 2.7.9.


N-queens problem solving time:

.. image:: https://raw.githubusercontent.com/kdeldycke/chessboard/develop/nqueens-performances.png
   :alt: N-queens problem solving time.
   :align: center
