#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2016 Kevin Deldycke <kevin@deldycke.com>
#                         and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import codecs
import os
import re

from setuptools import find_packages, setup

MODULE_NAME = 'chessboard'

DEPENDENCIES = [
    'click >= 5.0',
    'click_log',
    'bprofile',
    'numpy',
    'pandas',
    'seaborn',
    'py-cpuinfo',
]

EXTRA_DEPENDENCIES = {
    # Extra dependencies are made available through the
    # `$ pip install .[keyword]` command.
    'docs': [
        'sphinx >= 1.4',
        'sphinx_rtd_theme'],
    'tests': [
        'nose',
        'coverage'],
    'develop': [
        'pep8',
        'pylint',
        'isort',
        'wheel',
        'bumpversion'],
}


def get_version():

    with open(os.path.join(
        os.path.dirname(__file__), MODULE_NAME, '__init__.py')
    ) as init:

        for line in init.readlines():
            res = re.match(r'__version__ *= *[\'"]([0-9a-z\.]*)[\'"]$', line)
            if res:
                return res.group(1)


def get_long_description():
    readme = os.path.join(os.path.dirname(__file__), 'README.rst')
    changes = os.path.join(os.path.dirname(__file__), 'CHANGES.rst')
    return codecs.open(readme, encoding='utf-8').read() + '\n' + \
        codecs.open(changes, encoding='utf-8').read()


setup(
    name=MODULE_NAME,
    version=get_version(),
    description="CLI to solve combinatoric chess puzzles.",
    long_description=get_long_description(),

    author='Kevin Deldycke',
    author_email='kevin@deldycke.com',
    url='http://github.com/kdeldycke/chessboard',
    license='GPLv2+',

    packages=find_packages(),
    install_requires=DEPENDENCIES,
    tests_require=DEPENDENCIES + EXTRA_DEPENDENCIES['tests'],
    extras_require=EXTRA_DEPENDENCIES,
    dependency_links=[
    ],
    test_suite=MODULE_NAME + '.tests',

    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        # List of python versions and their support status:
        # https://en.wikipedia.org/wiki/CPython#Version_history
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Education',
        'Topic :: Games/Entertainment :: Board Games',
    ],

    entry_points={
        'console_scripts': [
            'chessboard=chessboard.cli:cli',
        ],
    }
)
