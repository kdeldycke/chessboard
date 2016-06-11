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

""" Benchmarking tools. """

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import platform
import time
from collections import OrderedDict
from os import path

import pandas
from numpy import median

import seaborn
from chessboard import PIECE_LABELS, SolverContext, __version__
from cpuinfo import get_cpu_info


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
    cpu_info = get_cpu_info()
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
        ('machine', platform.machine()),
        # CPU.
        ('cpu_vendor', cpu_info['vendor_id']),
        ('cpu_model', cpu_info['brand']),
        ('cpu_freq_actual', cpu_info['hz_actual'][0]),
        ('cpu_freq_advertised', cpu_info['hz_advertised'][0]),
        ('cpu_l2_cache', cpu_info['l2_cache_size']),
    ])

    # Sorted column IDs.
    column_ids = ['length', 'height'] + list(PIECE_LABELS) + [
        'solutions', 'execution_time'] + list(context)

    def __init__(self):
        """ Initialize the result database. """
        self.results = pandas.DataFrame(columns=self.column_ids)

    def load_csv(self):
        """ Load old benchmark results from CSV. """
        self.results = self.results.append(pandas.read_csv(self.csv_filepath))

    def add(self, new_results):
        """ Add new benchmark results. """
        for result in new_results:
            result.update(self.context)
            self.results = self.results.append(result, ignore_index=True)

    def save_csv(self):
        """ Dump all results to CSV. """
        # Sort results so we can start to see patterns right in the raw CSV.
        self.results.sort_values(by=self.column_ids, inplace=True)
        # Gotcha: integers seems to be promoted to float64 because of
        # reindexation. See: http://pandas.pydata.org/pandas-docs/stable
        # /gotchas.html#na-type-promotions
        self.results.reindex(columns=self.column_ids).to_csv(
            self.csv_filepath, index=False)

    def nqueen_graph(self):
        """ Graph n-queens problem for the current version and context. """
        # Filters out boards with pieces other than queens.
        nqueens = self.results
        for piece_label in set(PIECE_LABELS).difference(['queen']):
            nqueens = nqueens[nqueens[piece_label].map(pandas.isnull)]

        # Filters out non-square boards whose dimension are not aligned to the
        # number of queens.
        nqueens = nqueens[nqueens['length'] == nqueens['queen']]
        nqueens = nqueens[nqueens['height'] == nqueens['queen']]

        # Filters out results not obtained from this system.
        for label, value in self.context.items():
            if not value:
                nqueens = nqueens[nqueens[label].map(pandas.isnull)]
            else:
                nqueens = nqueens[nqueens[label] == value]

        plot = seaborn.factorplot(
            x='queen',
            y='execution_time',
            data=nqueens.sort(columns='queen'),
            estimator=median,
            kind='bar',
            palette='BuGn_d',
            aspect=1.5)
        plot.set_xlabels('Number of queens')
        plot.set_ylabels('Solving time in seconds (log scale)')
        plot.fig.get_axes()[0].set_yscale('log')

        plot.savefig('nqueens-performances.png')
