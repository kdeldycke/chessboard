# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Kevin Deldycke <kevin@deldycke.com> and contributors.
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

""" Benchmarking tools and scenarii. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import csv
import time
import platform
from os import path
from operator import methodcaller
from itertools import chain
import multiprocessing

from chessboard import __version__, SolverContext


scenarii = [
    # Tiny boards
    {'length': 3, 'height': 3, 'king': 2, 'rook': 1},
    {'length': 4, 'height': 4, 'rook': 2, 'knight': 4},
    # n queens problems.
    {'length': 1, 'height': 1, 'queen': 1},
    {'length': 2, 'height': 2, 'queen': 2},
    {'length': 3, 'height': 3, 'queen': 3},
    {'length': 4, 'height': 4, 'queen': 4},
    {'length': 5, 'height': 5, 'queen': 5},
    {'length': 6, 'height': 6, 'queen': 6},
    {'length': 7, 'height': 7, 'queen': 7},
    {'length': 8, 'height': 8, 'queen': 8},
    #{'length': 9, 'height': 9, 'queen': 9},
    # Big family.
    {'length': 5, 'height': 5,
     'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
    {'length': 6, 'height': 6,
     'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
    #{'length': 7, 'height': 7,
    # 'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
]


def run_scenario(params):
    """ Run one scenario and returns execution time and number of solutions.

    Also returns initial parameters in the response to keep the results
    associated with the initial context.
    """
    solver = SolverContext(**params)
    start = time.time()
    count = sum(1 for _ in solver.solve())
    execution_time = time.time() - start
    params.update({
        'solutions': count,
        'execution_time': execution_time})
    return params
