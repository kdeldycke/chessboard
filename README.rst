Chessboard
==========

Python CLI to explore chessboard positions.


TODO
----

* Implement a brute force algorithm.
* Make algorithm faster and smarter.


Development philosophy
----------------------

2. Then something that's beautiful.
3. Finally works on performance.


Install
-------

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ cd ./chessboard
    $ python ./setup.py develop


Usage
-----

.. code-block:: bash

    $ chessboard --help
    Usage: chessboard [OPTIONS]

      Python CLI to explore chessboard positions.

    Options:
      --version             Show the version and exit.
      -l, --length INTEGER  Length of the board.
      -h, --height INTEGER  Height of the board.
      -v, --verbose         Print much more debug statements.
      --king INTEGER        Number of kings to add to the board.
      --help                Show this message and exit.


Unit-tests
----------

.. code-block:: bash

      $ python ./setup.py nosetests


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
