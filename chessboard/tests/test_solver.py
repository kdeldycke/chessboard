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

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import unittest
from itertools import product, repeat
from operator import itemgetter

from chessboard import King, Permutations, Queen, SolverContext

from .. import PY2

if PY2:
    from itertools import izip
else:
    izip = zip


class TestPermutations(unittest.TestCase):

    def test_cartesian_product(self):
        self.assertSetEqual(
            set(map(frozenset, Permutations({'a': 1, 'b': 1, 'c': 1}))),
            set([frozenset(zip(*x)) for x in izip(
                repeat(list('abc')), product([0, 1, 2], repeat=3))]))

    def test_generator(self):
        gen = Permutations({'a': 1}, 3)
        self.assertEquals(
            [list(perm) for perm in gen],
            [[('a', 0)], [('a', 1)], [('a', 2)]])

    def test_skip_branch(self):
        gen = Permutations({'a': 1, 'b': 1, 'c': 2}, 5)

        results = []
        for perm in gen:
            perm = list(perm)
            for level, (_, position) in enumerate(perm):
                try:
                    if level == 1 and position == 2:
                        raise ValueError
                except ValueError:
                    gen.skip_branch(level)
                    break
            else:
                results.append(perm)

        self.assertEquals(results, [
            [('a', 0), ('b', 0), ('c', 0), ('c', 0)],
            [('a', 0), ('b', 0), ('c', 0), ('c', 1)],
            [('a', 0), ('b', 0), ('c', 0), ('c', 2)],
            [('a', 0), ('b', 0), ('c', 0), ('c', 3)],
            [('a', 0), ('b', 0), ('c', 0), ('c', 4)],
            [('a', 0), ('b', 0), ('c', 1), ('c', 1)],
            [('a', 0), ('b', 0), ('c', 1), ('c', 2)],
            [('a', 0), ('b', 0), ('c', 1), ('c', 3)],
            [('a', 0), ('b', 0), ('c', 1), ('c', 4)],
            [('a', 0), ('b', 0), ('c', 2), ('c', 2)],
            [('a', 0), ('b', 0), ('c', 2), ('c', 3)],
            [('a', 0), ('b', 0), ('c', 2), ('c', 4)],
            [('a', 0), ('b', 0), ('c', 3), ('c', 3)],
            [('a', 0), ('b', 0), ('c', 3), ('c', 4)],
            [('a', 0), ('b', 0), ('c', 4), ('c', 4)],
            [('a', 0), ('b', 1), ('c', 0), ('c', 0)],
            [('a', 0), ('b', 1), ('c', 0), ('c', 1)],
            [('a', 0), ('b', 1), ('c', 0), ('c', 2)],
            [('a', 0), ('b', 1), ('c', 0), ('c', 3)],
            [('a', 0), ('b', 1), ('c', 0), ('c', 4)],
            [('a', 0), ('b', 1), ('c', 1), ('c', 1)],
            [('a', 0), ('b', 1), ('c', 1), ('c', 2)],
            [('a', 0), ('b', 1), ('c', 1), ('c', 3)],
            [('a', 0), ('b', 1), ('c', 1), ('c', 4)],
            [('a', 0), ('b', 1), ('c', 2), ('c', 2)],
            [('a', 0), ('b', 1), ('c', 2), ('c', 3)],
            [('a', 0), ('b', 1), ('c', 2), ('c', 4)],
            [('a', 0), ('b', 1), ('c', 3), ('c', 3)],
            [('a', 0), ('b', 1), ('c', 3), ('c', 4)],
            [('a', 0), ('b', 1), ('c', 4), ('c', 4)],
            [('a', 0), ('b', 3), ('c', 0), ('c', 0)],
            [('a', 0), ('b', 3), ('c', 0), ('c', 1)],
            [('a', 0), ('b', 3), ('c', 0), ('c', 2)],
            [('a', 0), ('b', 3), ('c', 0), ('c', 3)],
            [('a', 0), ('b', 3), ('c', 0), ('c', 4)],
            [('a', 0), ('b', 3), ('c', 1), ('c', 1)],
            [('a', 0), ('b', 3), ('c', 1), ('c', 2)],
            [('a', 0), ('b', 3), ('c', 1), ('c', 3)],
            [('a', 0), ('b', 3), ('c', 1), ('c', 4)],
            [('a', 0), ('b', 3), ('c', 2), ('c', 2)],
            [('a', 0), ('b', 3), ('c', 2), ('c', 3)],
            [('a', 0), ('b', 3), ('c', 2), ('c', 4)],
            [('a', 0), ('b', 3), ('c', 3), ('c', 3)],
            [('a', 0), ('b', 3), ('c', 3), ('c', 4)],
            [('a', 0), ('b', 3), ('c', 4), ('c', 4)],
            [('a', 0), ('b', 4), ('c', 0), ('c', 0)],
            [('a', 0), ('b', 4), ('c', 0), ('c', 1)],
            [('a', 0), ('b', 4), ('c', 0), ('c', 2)],
            [('a', 0), ('b', 4), ('c', 0), ('c', 3)],
            [('a', 0), ('b', 4), ('c', 0), ('c', 4)],
            [('a', 0), ('b', 4), ('c', 1), ('c', 1)],
            [('a', 0), ('b', 4), ('c', 1), ('c', 2)],
            [('a', 0), ('b', 4), ('c', 1), ('c', 3)],
            [('a', 0), ('b', 4), ('c', 1), ('c', 4)],
            [('a', 0), ('b', 4), ('c', 2), ('c', 2)],
            [('a', 0), ('b', 4), ('c', 2), ('c', 3)],
            [('a', 0), ('b', 4), ('c', 2), ('c', 4)],
            [('a', 0), ('b', 4), ('c', 3), ('c', 3)],
            [('a', 0), ('b', 4), ('c', 3), ('c', 4)],
            [('a', 0), ('b', 4), ('c', 4), ('c', 4)],
            [('a', 1), ('b', 0), ('c', 0), ('c', 0)],
            [('a', 1), ('b', 0), ('c', 0), ('c', 1)],
            [('a', 1), ('b', 0), ('c', 0), ('c', 2)],
            [('a', 1), ('b', 0), ('c', 0), ('c', 3)],
            [('a', 1), ('b', 0), ('c', 0), ('c', 4)],
            [('a', 1), ('b', 0), ('c', 1), ('c', 1)],
            [('a', 1), ('b', 0), ('c', 1), ('c', 2)],
            [('a', 1), ('b', 0), ('c', 1), ('c', 3)],
            [('a', 1), ('b', 0), ('c', 1), ('c', 4)],
            [('a', 1), ('b', 0), ('c', 2), ('c', 2)],
            [('a', 1), ('b', 0), ('c', 2), ('c', 3)],
            [('a', 1), ('b', 0), ('c', 2), ('c', 4)],
            [('a', 1), ('b', 0), ('c', 3), ('c', 3)],
            [('a', 1), ('b', 0), ('c', 3), ('c', 4)],
            [('a', 1), ('b', 0), ('c', 4), ('c', 4)],
            [('a', 1), ('b', 1), ('c', 0), ('c', 0)],
            [('a', 1), ('b', 1), ('c', 0), ('c', 1)],
            [('a', 1), ('b', 1), ('c', 0), ('c', 2)],
            [('a', 1), ('b', 1), ('c', 0), ('c', 3)],
            [('a', 1), ('b', 1), ('c', 0), ('c', 4)],
            [('a', 1), ('b', 1), ('c', 1), ('c', 1)],
            [('a', 1), ('b', 1), ('c', 1), ('c', 2)],
            [('a', 1), ('b', 1), ('c', 1), ('c', 3)],
            [('a', 1), ('b', 1), ('c', 1), ('c', 4)],
            [('a', 1), ('b', 1), ('c', 2), ('c', 2)],
            [('a', 1), ('b', 1), ('c', 2), ('c', 3)],
            [('a', 1), ('b', 1), ('c', 2), ('c', 4)],
            [('a', 1), ('b', 1), ('c', 3), ('c', 3)],
            [('a', 1), ('b', 1), ('c', 3), ('c', 4)],
            [('a', 1), ('b', 1), ('c', 4), ('c', 4)],
            [('a', 1), ('b', 3), ('c', 0), ('c', 0)],
            [('a', 1), ('b', 3), ('c', 0), ('c', 1)],
            [('a', 1), ('b', 3), ('c', 0), ('c', 2)],
            [('a', 1), ('b', 3), ('c', 0), ('c', 3)],
            [('a', 1), ('b', 3), ('c', 0), ('c', 4)],
            [('a', 1), ('b', 3), ('c', 1), ('c', 1)],
            [('a', 1), ('b', 3), ('c', 1), ('c', 2)],
            [('a', 1), ('b', 3), ('c', 1), ('c', 3)],
            [('a', 1), ('b', 3), ('c', 1), ('c', 4)],
            [('a', 1), ('b', 3), ('c', 2), ('c', 2)],
            [('a', 1), ('b', 3), ('c', 2), ('c', 3)],
            [('a', 1), ('b', 3), ('c', 2), ('c', 4)],
            [('a', 1), ('b', 3), ('c', 3), ('c', 3)],
            [('a', 1), ('b', 3), ('c', 3), ('c', 4)],
            [('a', 1), ('b', 3), ('c', 4), ('c', 4)],
            [('a', 1), ('b', 4), ('c', 0), ('c', 0)],
            [('a', 1), ('b', 4), ('c', 0), ('c', 1)],
            [('a', 1), ('b', 4), ('c', 0), ('c', 2)],
            [('a', 1), ('b', 4), ('c', 0), ('c', 3)],
            [('a', 1), ('b', 4), ('c', 0), ('c', 4)],
            [('a', 1), ('b', 4), ('c', 1), ('c', 1)],
            [('a', 1), ('b', 4), ('c', 1), ('c', 2)],
            [('a', 1), ('b', 4), ('c', 1), ('c', 3)],
            [('a', 1), ('b', 4), ('c', 1), ('c', 4)],
            [('a', 1), ('b', 4), ('c', 2), ('c', 2)],
            [('a', 1), ('b', 4), ('c', 2), ('c', 3)],
            [('a', 1), ('b', 4), ('c', 2), ('c', 4)],
            [('a', 1), ('b', 4), ('c', 3), ('c', 3)],
            [('a', 1), ('b', 4), ('c', 3), ('c', 4)],
            [('a', 1), ('b', 4), ('c', 4), ('c', 4)],
            [('a', 2), ('b', 0), ('c', 0), ('c', 0)],
            [('a', 2), ('b', 0), ('c', 0), ('c', 1)],
            [('a', 2), ('b', 0), ('c', 0), ('c', 2)],
            [('a', 2), ('b', 0), ('c', 0), ('c', 3)],
            [('a', 2), ('b', 0), ('c', 0), ('c', 4)],
            [('a', 2), ('b', 0), ('c', 1), ('c', 1)],
            [('a', 2), ('b', 0), ('c', 1), ('c', 2)],
            [('a', 2), ('b', 0), ('c', 1), ('c', 3)],
            [('a', 2), ('b', 0), ('c', 1), ('c', 4)],
            [('a', 2), ('b', 0), ('c', 2), ('c', 2)],
            [('a', 2), ('b', 0), ('c', 2), ('c', 3)],
            [('a', 2), ('b', 0), ('c', 2), ('c', 4)],
            [('a', 2), ('b', 0), ('c', 3), ('c', 3)],
            [('a', 2), ('b', 0), ('c', 3), ('c', 4)],
            [('a', 2), ('b', 0), ('c', 4), ('c', 4)],
            [('a', 2), ('b', 1), ('c', 0), ('c', 0)],
            [('a', 2), ('b', 1), ('c', 0), ('c', 1)],
            [('a', 2), ('b', 1), ('c', 0), ('c', 2)],
            [('a', 2), ('b', 1), ('c', 0), ('c', 3)],
            [('a', 2), ('b', 1), ('c', 0), ('c', 4)],
            [('a', 2), ('b', 1), ('c', 1), ('c', 1)],
            [('a', 2), ('b', 1), ('c', 1), ('c', 2)],
            [('a', 2), ('b', 1), ('c', 1), ('c', 3)],
            [('a', 2), ('b', 1), ('c', 1), ('c', 4)],
            [('a', 2), ('b', 1), ('c', 2), ('c', 2)],
            [('a', 2), ('b', 1), ('c', 2), ('c', 3)],
            [('a', 2), ('b', 1), ('c', 2), ('c', 4)],
            [('a', 2), ('b', 1), ('c', 3), ('c', 3)],
            [('a', 2), ('b', 1), ('c', 3), ('c', 4)],
            [('a', 2), ('b', 1), ('c', 4), ('c', 4)],
            [('a', 2), ('b', 3), ('c', 0), ('c', 0)],
            [('a', 2), ('b', 3), ('c', 0), ('c', 1)],
            [('a', 2), ('b', 3), ('c', 0), ('c', 2)],
            [('a', 2), ('b', 3), ('c', 0), ('c', 3)],
            [('a', 2), ('b', 3), ('c', 0), ('c', 4)],
            [('a', 2), ('b', 3), ('c', 1), ('c', 1)],
            [('a', 2), ('b', 3), ('c', 1), ('c', 2)],
            [('a', 2), ('b', 3), ('c', 1), ('c', 3)],
            [('a', 2), ('b', 3), ('c', 1), ('c', 4)],
            [('a', 2), ('b', 3), ('c', 2), ('c', 2)],
            [('a', 2), ('b', 3), ('c', 2), ('c', 3)],
            [('a', 2), ('b', 3), ('c', 2), ('c', 4)],
            [('a', 2), ('b', 3), ('c', 3), ('c', 3)],
            [('a', 2), ('b', 3), ('c', 3), ('c', 4)],
            [('a', 2), ('b', 3), ('c', 4), ('c', 4)],
            [('a', 2), ('b', 4), ('c', 0), ('c', 0)],
            [('a', 2), ('b', 4), ('c', 0), ('c', 1)],
            [('a', 2), ('b', 4), ('c', 0), ('c', 2)],
            [('a', 2), ('b', 4), ('c', 0), ('c', 3)],
            [('a', 2), ('b', 4), ('c', 0), ('c', 4)],
            [('a', 2), ('b', 4), ('c', 1), ('c', 1)],
            [('a', 2), ('b', 4), ('c', 1), ('c', 2)],
            [('a', 2), ('b', 4), ('c', 1), ('c', 3)],
            [('a', 2), ('b', 4), ('c', 1), ('c', 4)],
            [('a', 2), ('b', 4), ('c', 2), ('c', 2)],
            [('a', 2), ('b', 4), ('c', 2), ('c', 3)],
            [('a', 2), ('b', 4), ('c', 2), ('c', 4)],
            [('a', 2), ('b', 4), ('c', 3), ('c', 3)],
            [('a', 2), ('b', 4), ('c', 3), ('c', 4)],
            [('a', 2), ('b', 4), ('c', 4), ('c', 4)],
            [('a', 3), ('b', 0), ('c', 0), ('c', 0)],
            [('a', 3), ('b', 0), ('c', 0), ('c', 1)],
            [('a', 3), ('b', 0), ('c', 0), ('c', 2)],
            [('a', 3), ('b', 0), ('c', 0), ('c', 3)],
            [('a', 3), ('b', 0), ('c', 0), ('c', 4)],
            [('a', 3), ('b', 0), ('c', 1), ('c', 1)],
            [('a', 3), ('b', 0), ('c', 1), ('c', 2)],
            [('a', 3), ('b', 0), ('c', 1), ('c', 3)],
            [('a', 3), ('b', 0), ('c', 1), ('c', 4)],
            [('a', 3), ('b', 0), ('c', 2), ('c', 2)],
            [('a', 3), ('b', 0), ('c', 2), ('c', 3)],
            [('a', 3), ('b', 0), ('c', 2), ('c', 4)],
            [('a', 3), ('b', 0), ('c', 3), ('c', 3)],
            [('a', 3), ('b', 0), ('c', 3), ('c', 4)],
            [('a', 3), ('b', 0), ('c', 4), ('c', 4)],
            [('a', 3), ('b', 1), ('c', 0), ('c', 0)],
            [('a', 3), ('b', 1), ('c', 0), ('c', 1)],
            [('a', 3), ('b', 1), ('c', 0), ('c', 2)],
            [('a', 3), ('b', 1), ('c', 0), ('c', 3)],
            [('a', 3), ('b', 1), ('c', 0), ('c', 4)],
            [('a', 3), ('b', 1), ('c', 1), ('c', 1)],
            [('a', 3), ('b', 1), ('c', 1), ('c', 2)],
            [('a', 3), ('b', 1), ('c', 1), ('c', 3)],
            [('a', 3), ('b', 1), ('c', 1), ('c', 4)],
            [('a', 3), ('b', 1), ('c', 2), ('c', 2)],
            [('a', 3), ('b', 1), ('c', 2), ('c', 3)],
            [('a', 3), ('b', 1), ('c', 2), ('c', 4)],
            [('a', 3), ('b', 1), ('c', 3), ('c', 3)],
            [('a', 3), ('b', 1), ('c', 3), ('c', 4)],
            [('a', 3), ('b', 1), ('c', 4), ('c', 4)],
            [('a', 3), ('b', 3), ('c', 0), ('c', 0)],
            [('a', 3), ('b', 3), ('c', 0), ('c', 1)],
            [('a', 3), ('b', 3), ('c', 0), ('c', 2)],
            [('a', 3), ('b', 3), ('c', 0), ('c', 3)],
            [('a', 3), ('b', 3), ('c', 0), ('c', 4)],
            [('a', 3), ('b', 3), ('c', 1), ('c', 1)],
            [('a', 3), ('b', 3), ('c', 1), ('c', 2)],
            [('a', 3), ('b', 3), ('c', 1), ('c', 3)],
            [('a', 3), ('b', 3), ('c', 1), ('c', 4)],
            [('a', 3), ('b', 3), ('c', 2), ('c', 2)],
            [('a', 3), ('b', 3), ('c', 2), ('c', 3)],
            [('a', 3), ('b', 3), ('c', 2), ('c', 4)],
            [('a', 3), ('b', 3), ('c', 3), ('c', 3)],
            [('a', 3), ('b', 3), ('c', 3), ('c', 4)],
            [('a', 3), ('b', 3), ('c', 4), ('c', 4)],
            [('a', 3), ('b', 4), ('c', 0), ('c', 0)],
            [('a', 3), ('b', 4), ('c', 0), ('c', 1)],
            [('a', 3), ('b', 4), ('c', 0), ('c', 2)],
            [('a', 3), ('b', 4), ('c', 0), ('c', 3)],
            [('a', 3), ('b', 4), ('c', 0), ('c', 4)],
            [('a', 3), ('b', 4), ('c', 1), ('c', 1)],
            [('a', 3), ('b', 4), ('c', 1), ('c', 2)],
            [('a', 3), ('b', 4), ('c', 1), ('c', 3)],
            [('a', 3), ('b', 4), ('c', 1), ('c', 4)],
            [('a', 3), ('b', 4), ('c', 2), ('c', 2)],
            [('a', 3), ('b', 4), ('c', 2), ('c', 3)],
            [('a', 3), ('b', 4), ('c', 2), ('c', 4)],
            [('a', 3), ('b', 4), ('c', 3), ('c', 3)],
            [('a', 3), ('b', 4), ('c', 3), ('c', 4)],
            [('a', 3), ('b', 4), ('c', 4), ('c', 4)],
            [('a', 4), ('b', 0), ('c', 0), ('c', 0)],
            [('a', 4), ('b', 0), ('c', 0), ('c', 1)],
            [('a', 4), ('b', 0), ('c', 0), ('c', 2)],
            [('a', 4), ('b', 0), ('c', 0), ('c', 3)],
            [('a', 4), ('b', 0), ('c', 0), ('c', 4)],
            [('a', 4), ('b', 0), ('c', 1), ('c', 1)],
            [('a', 4), ('b', 0), ('c', 1), ('c', 2)],
            [('a', 4), ('b', 0), ('c', 1), ('c', 3)],
            [('a', 4), ('b', 0), ('c', 1), ('c', 4)],
            [('a', 4), ('b', 0), ('c', 2), ('c', 2)],
            [('a', 4), ('b', 0), ('c', 2), ('c', 3)],
            [('a', 4), ('b', 0), ('c', 2), ('c', 4)],
            [('a', 4), ('b', 0), ('c', 3), ('c', 3)],
            [('a', 4), ('b', 0), ('c', 3), ('c', 4)],
            [('a', 4), ('b', 0), ('c', 4), ('c', 4)],
            [('a', 4), ('b', 1), ('c', 0), ('c', 0)],
            [('a', 4), ('b', 1), ('c', 0), ('c', 1)],
            [('a', 4), ('b', 1), ('c', 0), ('c', 2)],
            [('a', 4), ('b', 1), ('c', 0), ('c', 3)],
            [('a', 4), ('b', 1), ('c', 0), ('c', 4)],
            [('a', 4), ('b', 1), ('c', 1), ('c', 1)],
            [('a', 4), ('b', 1), ('c', 1), ('c', 2)],
            [('a', 4), ('b', 1), ('c', 1), ('c', 3)],
            [('a', 4), ('b', 1), ('c', 1), ('c', 4)],
            [('a', 4), ('b', 1), ('c', 2), ('c', 2)],
            [('a', 4), ('b', 1), ('c', 2), ('c', 3)],
            [('a', 4), ('b', 1), ('c', 2), ('c', 4)],
            [('a', 4), ('b', 1), ('c', 3), ('c', 3)],
            [('a', 4), ('b', 1), ('c', 3), ('c', 4)],
            [('a', 4), ('b', 1), ('c', 4), ('c', 4)],
            [('a', 4), ('b', 3), ('c', 0), ('c', 0)],
            [('a', 4), ('b', 3), ('c', 0), ('c', 1)],
            [('a', 4), ('b', 3), ('c', 0), ('c', 2)],
            [('a', 4), ('b', 3), ('c', 0), ('c', 3)],
            [('a', 4), ('b', 3), ('c', 0), ('c', 4)],
            [('a', 4), ('b', 3), ('c', 1), ('c', 1)],
            [('a', 4), ('b', 3), ('c', 1), ('c', 2)],
            [('a', 4), ('b', 3), ('c', 1), ('c', 3)],
            [('a', 4), ('b', 3), ('c', 1), ('c', 4)],
            [('a', 4), ('b', 3), ('c', 2), ('c', 2)],
            [('a', 4), ('b', 3), ('c', 2), ('c', 3)],
            [('a', 4), ('b', 3), ('c', 2), ('c', 4)],
            [('a', 4), ('b', 3), ('c', 3), ('c', 3)],
            [('a', 4), ('b', 3), ('c', 3), ('c', 4)],
            [('a', 4), ('b', 3), ('c', 4), ('c', 4)],
            [('a', 4), ('b', 4), ('c', 0), ('c', 0)],
            [('a', 4), ('b', 4), ('c', 0), ('c', 1)],
            [('a', 4), ('b', 4), ('c', 0), ('c', 2)],
            [('a', 4), ('b', 4), ('c', 0), ('c', 3)],
            [('a', 4), ('b', 4), ('c', 0), ('c', 4)],
            [('a', 4), ('b', 4), ('c', 1), ('c', 1)],
            [('a', 4), ('b', 4), ('c', 1), ('c', 2)],
            [('a', 4), ('b', 4), ('c', 1), ('c', 3)],
            [('a', 4), ('b', 4), ('c', 1), ('c', 4)],
            [('a', 4), ('b', 4), ('c', 2), ('c', 2)],
            [('a', 4), ('b', 4), ('c', 2), ('c', 3)],
            [('a', 4), ('b', 4), ('c', 2), ('c', 4)],
            [('a', 4), ('b', 4), ('c', 3), ('c', 3)],
            [('a', 4), ('b', 4), ('c', 3), ('c', 4)],
            [('a', 4), ('b', 4), ('c', 4), ('c', 4)]])


class TestSolverContext(unittest.TestCase):

    def test_instanciation(self):
        solver = SolverContext(3, 3, king=2, queen=7)
        self.assertEquals(solver.length, 3)
        self.assertEquals(solver.height, 3)
        self.assertDictContainsSubset(
            {King.uid: 2, Queen.uid: 7}, solver.pieces)

    def check_results(self, results, expected):
        """ Check found results.

        Normalize result sets into hashable sets so we can make them easily
        comparable.
        """
        normalized_expected = set([tuple(sorted(
            r,
            key=itemgetter(0, 1, 2)))
            for r in expected])
        normalized_results = set([tuple(sorted([
            (p.__class__.__name__, p.x, p.y) for p in r.pieces],
            key=itemgetter(0, 1, 2)))
            for r in results])
        self.assertEquals(len(normalized_results), len(expected))
        self.assertSetEqual(normalized_results, normalized_expected)

    def test_tinyest_board(self):
        solver = SolverContext(1, 1, king=1)
        results = solver.solve()
        self.check_results(results, [
            [('King', 0, 0)],
        ])
        self.assertEquals(solver.result_counter, 1)

    def test_single_king(self):
        solver = SolverContext(3, 3, king=1)
        results = solver.solve()
        self.check_results(results, [
            [('King', 0, 0)],
            [('King', 0, 1)],
            [('King', 0, 2)],
            [('King', 1, 0)],
            [('King', 1, 1)],
            [('King', 1, 2)],
            [('King', 2, 0)],
            [('King', 2, 1)],
            [('King', 2, 2)],
        ])
        self.assertEquals(solver.result_counter, 9)

    def test_wide_board(self):
        solver = SolverContext(4, 1, king=1)
        results = solver.solve()
        self.check_results(results, [
            [('King', 0, 0)],
            [('King', 1, 0)],
            [('King', 2, 0)],
            [('King', 3, 0)],
        ])
        self.assertEquals(solver.result_counter, 4)

    def test_long_board(self):
        solver = SolverContext(1, 4, king=1)
        results = solver.solve()
        self.check_results(results, [
            [('King', 0, 0)],
            [('King', 0, 1)],
            [('King', 0, 2)],
            [('King', 0, 3)],
        ])
        self.assertEquals(solver.result_counter, 4)

    def test_single_queen(self):
        solver = SolverContext(3, 3, queen=1)
        results = solver.solve()
        self.check_results(results, [
            [('Queen', 0, 0)],
            [('Queen', 0, 1)],
            [('Queen', 0, 2)],
            [('Queen', 1, 0)],
            [('Queen', 1, 1)],
            [('Queen', 1, 2)],
            [('Queen', 2, 0)],
            [('Queen', 2, 1)],
            [('Queen', 2, 2)],
        ])
        self.assertEquals(solver.result_counter, 9)

    def test_no_queen_solutions(self):
        solver = SolverContext(3, 3, queen=3)
        results = solver.solve()
        self.check_results(results, [])
        self.assertEquals(solver.result_counter, 0)

    def test_two_kings_one_rook(self):
        solver = SolverContext(3, 3, king=2, rook=1)
        results = solver.solve()
        self.check_results(results, [
            [('King', 0, 0), ('King', 2, 0), ('Rook', 1, 2)],
            [('King', 0, 0), ('King', 0, 2), ('Rook', 2, 1)],
            [('King', 2, 0), ('King', 2, 2), ('Rook', 0, 1)],
            [('King', 0, 2), ('King', 2, 2), ('Rook', 1, 0)],
        ])
        self.assertEquals(solver.result_counter, 4)

    def test_two_rooks_four_knights(self):
        solver = SolverContext(4, 4, rook=2, knight=4)
        results = solver.solve()
        self.check_results(results, [
            [('Rook', 0, 3), ('Rook', 2, 1),
             ('Knight', 1, 0), ('Knight', 3, 0),
             ('Knight', 1, 2), ('Knight', 3, 2)],
            [('Rook', 0, 1), ('Rook', 2, 3),
             ('Knight', 1, 0), ('Knight', 3, 0),
             ('Knight', 1, 2), ('Knight', 3, 2)],
            [('Rook', 0, 0), ('Rook', 2, 2),
             ('Knight', 1, 1), ('Knight', 3, 1),
             ('Knight', 1, 3), ('Knight', 3, 3)],
            [('Rook', 0, 2), ('Rook', 2, 0),
             ('Knight', 1, 1), ('Knight', 3, 1),
             ('Knight', 1, 3), ('Knight', 3, 3)],
            [('Rook', 1, 0), ('Rook', 3, 2),
             ('Knight', 0, 1), ('Knight', 2, 1),
             ('Knight', 0, 3), ('Knight', 2, 3)],
            [('Rook', 3, 0), ('Rook', 1, 2),
             ('Knight', 0, 1), ('Knight', 2, 1),
             ('Knight', 0, 3), ('Knight', 2, 3)],
            [('Rook', 1, 3), ('Rook', 3, 1),
             ('Knight', 0, 0), ('Knight', 2, 0),
             ('Knight', 0, 2), ('Knight', 2, 2)],
            [('Rook', 1, 1), ('Rook', 3, 3),
             ('Knight', 0, 0), ('Knight', 2, 0),
             ('Knight', 0, 2), ('Knight', 2, 2)],
        ])
        self.assertEquals(solver.result_counter, 8)

    @unittest.skip("Solver too slow")
    def test_eight_queens(self):
        solver = SolverContext(8, 8, queen=8)
        for _ in solver.solve():
            pass
        self.assertEquals(solver.result_counter, 92)

    @unittest.skip("Solver too slow")
    def test_big_family(self):
        solver = SolverContext(7, 7, king=2, queen=2, bishop=2, knight=1)
        for _ in solver.solve():
            pass
        self.assertEquals(solver.result_counter, 1000000)
