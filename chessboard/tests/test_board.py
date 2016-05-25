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

from chessboard import Board, ForbiddenCoordinates, ForbiddenIndex


class TestBoard(unittest.TestCase):

    def test_all_positions(self):
        self.assertEquals(list(Board(3, 3).positions), [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2), (2, 2)])

    def test_coord_to_index(self):
        self.assertEquals(Board(3, 3).coordinates_to_index(0, 0), 0)
        self.assertEquals(Board(3, 3).coordinates_to_index(1, 1), 4)
        self.assertEquals(Board(3, 3).coordinates_to_index(2, 2), 8)

    def test_translate_error(self):
        with self.assertRaises(ForbiddenCoordinates):
            Board(3, 3).coordinates_to_index(-1, 0)
        with self.assertRaises(ForbiddenCoordinates):
            Board(3, 3).coordinates_to_index(0, -1)
        with self.assertRaises(ForbiddenCoordinates):
            Board(3, 3).coordinates_to_index(0, 3)
        with self.assertRaises(ForbiddenCoordinates):
            Board(3, 3).coordinates_to_index(3, 0)

    def test_index_to_coord(self):
        self.assertEquals(Board(3, 3).index_to_coordinates(0), (0, 0))
        self.assertEquals(Board(3, 3).index_to_coordinates(1), (1, 0))
        self.assertEquals(Board(3, 3).index_to_coordinates(2), (2, 0))
        self.assertEquals(Board(3, 3).index_to_coordinates(3), (0, 1))
        self.assertEquals(Board(3, 3).index_to_coordinates(4), (1, 1))
        self.assertEquals(Board(3, 3).index_to_coordinates(5), (2, 1))
        self.assertEquals(Board(3, 3).index_to_coordinates(6), (0, 2))
        self.assertEquals(Board(3, 3).index_to_coordinates(7), (1, 2))
        self.assertEquals(Board(3, 3).index_to_coordinates(8), (2, 2))

    def test_wide_index_to_coord(self):
        self.assertEquals(Board(1, 4).index_to_coordinates(0), (0, 0))
        self.assertEquals(Board(1, 4).index_to_coordinates(1), (0, 1))
        self.assertEquals(Board(1, 4).index_to_coordinates(2), (0, 2))
        self.assertEquals(Board(1, 4).index_to_coordinates(3), (0, 3))

    def test_long_index_to_coord(self):
        self.assertEquals(Board(4, 1).index_to_coordinates(0), (0, 0))
        self.assertEquals(Board(4, 1).index_to_coordinates(1), (1, 0))
        self.assertEquals(Board(4, 1).index_to_coordinates(2), (2, 0))
        self.assertEquals(Board(4, 1).index_to_coordinates(3), (3, 0))

    def test_index_to_coord_error(self):
        with self.assertRaises(ForbiddenIndex):
            Board(3, 3).index_to_coordinates(-1)
        with self.assertRaises(ForbiddenIndex):
            Board(3, 3).index_to_coordinates(9)
