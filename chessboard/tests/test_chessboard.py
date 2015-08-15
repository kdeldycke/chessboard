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

from __future__ import (unicode_literals, print_function, absolute_import,
                        division)

from operator import itemgetter
import unittest

from chessboard import Chessboard, Board, ForbiddenIndex, ForbiddenCoordinates


class TestChessboard(unittest.TestCase):

    def test_instanciation(self):
        board = Chessboard(3, 3, king=2, queen=7)
        self.assertEquals(board.length, 3)
        self.assertEquals(board.height, 3)
        self.assertDictContainsSubset({'king': 2, 'queen': 7}, board.pieces)

    def test_tree(self):
        self.assertEquals(
            list(Chessboard.tree('abc')),
            ['a', 'b', 'c'])

        self.assertEquals(
            [list(i) for i in list(Chessboard.tree('abc', 'cde'))], [
                ['a', 'c'],
                ['a', 'd'],
                ['a', 'e'],
                ['b', 'c'],
                ['b', 'd'],
                ['b', 'e'],
                ['c', 'c'],
                ['c', 'd'],
                ['c', 'e'],
            ])


class TestSolver(unittest.TestCase):

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
        board = Chessboard(1, 1, king=1)
        results = board.solve()
        self.check_results(results, [
            [('King', 0, 0)],
        ])

    def test_single_king(self):
        board = Chessboard(3, 3, king=1)
        results = board.solve()
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

    def test_wide_board(self):
        board = Chessboard(4, 1, king=1)
        results = board.solve()
        self.check_results(results, [
            [('King', 0, 0)],
            [('King', 1, 0)],
            [('King', 2, 0)],
            [('King', 3, 0)],
        ])

    def test_long_board(self):
        board = Chessboard(1, 4, king=1)
        results = board.solve()
        self.check_results(results, [
            [('King', 0, 0)],
            [('King', 0, 1)],
            [('King', 0, 2)],
            [('King', 0, 3)],
        ])

    def test_single_queen(self):
        board = Chessboard(3, 3, queen=1)
        results = board.solve()
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

    def test_no_queen_solutions(self):
        board = Chessboard(3, 3, queen=3)
        results = board.solve()
        self.check_results(results, [])

    def test_two_kings_one_rook(self):
        board = Chessboard(3, 3, king=2, rook=1)
        results = board.solve()
        self.check_results(results, [
            [('King', 0, 0), ('King', 2, 0), ('Rook', 1, 2)],
            [('King', 0, 0), ('King', 0, 2), ('Rook', 2, 1)],
            [('King', 2, 0), ('King', 2, 2), ('Rook', 0, 1)],
            [('King', 0, 2), ('King', 2, 2), ('Rook', 1, 0)],
        ])

    def test_two_rooks_four_knights(self):
        board = Chessboard(4, 4, rook=2, knight=4)
        results = board.solve()
        self.check_results(results, [
            [('Rook', 0, 3), ('Rook', 2, 1),
             ('Knight', 1, 0), ('Knight', 3, 0), ('Knight', 1, 2), ('Knight', 3, 2)],
            [('Rook', 0, 1), ('Rook', 2, 3),
             ('Knight', 1, 0), ('Knight', 3, 0), ('Knight', 1, 2), ('Knight', 3, 2)],
            [('Rook', 0, 0), ('Rook', 2, 2),
             ('Knight', 1, 1), ('Knight', 3, 1), ('Knight', 1, 3), ('Knight', 3, 3)],
            [('Rook', 0, 2), ('Rook', 2, 0),
             ('Knight', 1, 1), ('Knight', 3, 1), ('Knight', 1, 3), ('Knight', 3, 3)],
            [('Rook', 1, 0), ('Rook', 3, 2),
             ('Knight', 0, 1), ('Knight', 2, 1), ('Knight', 0, 3), ('Knight', 2, 3)],
            [('Rook', 3, 0), ('Rook', 1, 2),
             ('Knight', 0, 1), ('Knight', 2, 1), ('Knight', 0, 3), ('Knight', 2, 3)],
            [('Rook', 1, 3), ('Rook', 3, 1),
             ('Knight', 0, 0), ('Knight', 2, 0), ('Knight', 0, 2), ('Knight', 2, 2)],
            [('Rook', 1, 1), ('Rook', 3, 3),
             ('Knight', 0, 0), ('Knight', 2, 0), ('Knight', 0, 2), ('Knight', 2, 2)],
       ])

    @unittest.skip("Solver too slow")
    def test_big_family(self):
        board = Chessboard(7, 7, king=2, queen=2, bishop=2, knight=1)
        results = board.solve()


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
