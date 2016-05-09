Development
===========

Stable release: |release| |dependencies| |license| |popularity|

Development: |build| |docs| |coverage| |quality|

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
.. |docs| image:: https://readthedocs.org/projects/chessboard/badge/?version=develop
    :target: http://chessboard.readthedocs.io/en/develop/
    :alt: Documentation Status
.. |coverage| image:: https://codecov.io/github/kdeldycke/chessboard/coverage.svg?branch=develop
    :target: https://codecov.io/github/kdeldycke/chessboard?branch=develop
    :alt: Coverage Status
.. |quality| image:: https://img.shields.io/scrutinizer/g/kdeldycke/chessboard.svg?style=flat
    :target: https://scrutinizer-ci.com/g/kdeldycke/chessboard/?branch=develop
    :alt: Code Quality


Philosophy
----------

1. First create something that work (to provide business value).
2. Then something that's beautiful (to lower maintenance costs).
3. Finally works on performance (to avoid wasting time on premature
   optimizations).


Setup a local development environment
-------------------------------------

Check out latest development branch:

.. code-block:: bash

    $ git clone git@github.com:kdeldycke/chessboard.git
    $ cd ./chessboard
    $ python ./setup.py develop

Run unit-tests:

.. code-block:: bash

    $ python ./setup.py nosetests

Run `isort <https://pep8.readthedocs.org>`_ utility to sort Python imports:

.. code-block:: bash

    $ pip install isort
    $ isort --apply

Run `PEP8 <https://pep8.readthedocs.org>`_ and `Pylint
<http://docs.pylint.org>`_ code style checks:

.. code-block:: bash

    $ pip install pep8 pylint
    $ pep8 chessboard
    $ pylint --rcfile=setup.cfg chessboard

Build local documentation with `Sphinx <http://www.sphinx-doc.org>`_:

.. code-block:: bash

    $ pip install sphinx sphinx_rtd_theme
    $ sphinx-apidoc -f -o ./docs .
    $ sphinx-build -b html ./docs ./docs/html


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
    $ python ./setup.py clean
    $ rm -rf ./build ./dist
    $ python ./setup.py sdist bdist_egg bdist_wheel upload -r testpypi

Publish packaging to `PyPi <https://pypi.python.org>`_:

.. code-block:: bash

    $ python ./setup.py register -r pypi
    $ python ./setup.py clean
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
