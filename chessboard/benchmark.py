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

""" Benchmarking tools. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import csv
from collections import OrderedDict
import time
import platform
from os import path

from chessboard import __version__, SolverContext, PIECE_LABELS


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


class Benchmark(object):

    """ Defines benchmark suite and utility to save and render the results. """

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
        # {'length': 9, 'height': 9, 'queen': 9},
        # Big family.
        {'length': 5, 'height': 5,
         'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
        {'length': 6, 'height': 6,
         'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
        # {'length': 7, 'height': 7,
        #  'king': 2, 'queen': 2, 'bishop': 2, 'knight': 1},
    ]

    # Data are going in a CSV file along this file.
    csv_filepath = path.join(path.dirname(__file__), 'benchmark.csv')

    # Gather software and hardware metadata.
    context = OrderedDict([
        # Solver.
        ('chessboard', __version__),
        # Python interpreter.
        ('implementation', platform.python_implementation()),
        ('python', platform.python_version()),
        # Underlaying OS.
        ('system', platform.system()),
        ('osx', platform.mac_ver()[0]),
        ('linux', ' '.join(platform.linux_distribution()).strip()),
        ('windows', platform.win32_ver()[1]),
        ('java', platform.java_ver()[0]),
        # Hardware.
        ('architecture', platform.architecture()[0]),
        ('machine', platform.machine())])

    # Sorted column IDs.
    column_ids = ['length', 'height'] + PIECE_LABELS.keys() + [
        'solutions', 'execution_time'] + context.keys()

    def __init__(self):
        """ Initialize the result database. """
        self.database = []

    def load_csv(self):
        """ Load old benchmark results from CSV. """
        if path.exists(self.csv_filepath):
            with open(self.csv_filepath, 'rb') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.database.append(row)

    def add(self, new_results):
        """ Add new benchmark results. """
        for result in new_results:
            result.update(self.context)
            self.database.append(result)

    def save_csv(self):
        """ Dump all results to CSV. """
        with open(self.csv_filepath, 'wb') as csv_file:
            writer = csv.DictWriter(csv_file, self.column_ids)
            writer.writeheader()
            writer.writerows(self.database)
