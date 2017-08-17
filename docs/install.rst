Installation
============


Dependencies
------------

This software depends on the following non-Python packages:

* `Graphviz <http://graphviz.org>`_.

You'll find below several ways of installing these dependencies on all major
OSes.

### macOS

All dependencies are available through `HomeBrew <https://brew.sh/>`_:

.. code-block:: shell-session

    $ brew install graphviz

### Linux

All dependencies are available via your favorite distribution package manager.

Be it Ubuntu or Debian:

.. code-block:: shell-session

    $ sudo apt install graphviz

Or Fedora:

.. code-block:: shell-session

    $ dnf install graphviz

### Windows

All dependencies are available through `Chocolatey <https://chocolatey.org>`_:

.. code-block:: ps1con

   C:\> choco install graphviz


Installing `chessboard`
-----------------------

This package is `available on PyPi <https://pypi.python.org/pypi/chessboard>`_,
so you can install the latest stable release and its python dependencies with a
simple ``pip`` call:

.. code-block:: shell-session

    $ pip install chessboard

In case ``pip`` is not installed on your system, see `pip installation
instructions <https://pip.pypa.io/en/stable/installing/>`_.


Python dependencies
-------------------

FYI, here is a graph of Python package dependencies:

.. image:: dependencies.png
   :alt: Package dependency graph
   :align: center
