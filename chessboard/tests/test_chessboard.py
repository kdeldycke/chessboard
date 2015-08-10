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

import unittest

from chessboard import Chessboard
from chessboard.chessboard import Board


class TestChessboard(unittest.TestCase):

    def test_instanciation(self):
        board = Chessboard(3, 3, king=2, queen=7)
        self.assertEquals(board.length, 3)
        self.assertEquals(board.height, 3)
        self.assertDictContainsSubset({'king': 2, 'queen': 7}, board.pieces)



class TestBoard(unittest.TestCase):

    def test_validate_position(self):
        """ Test validation of 2D position. """
        Board(3, 3).validate_position(0, 0)
        Board(3, 3).validate_position(0, 2)
        Board(3, 3).validate_position(2, 0)
        Board(3, 3).validate_position(2, 2)
        with self.assertRaises(ValueError):
            Board(3, 3).validate_position(-1, 0)
        with self.assertRaises(ValueError):
            Board(3, 3).validate_position(0, -1)
        with self.assertRaises(ValueError):
            Board(3, 3).validate_position(0, 3)
        with self.assertRaises(ValueError):
            Board(3, 3).validate_position(3, 0)
