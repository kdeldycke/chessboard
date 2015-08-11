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

from chessboard import Board, King


class TestKing(unittest.TestCase):

    def test_translate(self):
        """ Test computation of translation and position conversion.
        """
        self.assertEquals(King(0, 0).translate(Board(3, 3)), 0)
        self.assertEquals(King(1, 1).translate(Board(3, 3)), 4)
        self.assertEquals(King(2, 2).translate(Board(3, 3)), 8)

    def test_translate_error(self):
        with self.assertRaises(ValueError):
            King(0, 5).translate(Board(3, 3))
        with self.assertRaises(ValueError):
            King(5, 0).translate(Board(3, 3))

    def test_territory(self):
        """ Test computation of territory at the center and cardinal points.
        """
        self.assertEquals(King(1, 1).territory(Board(3, 3)), [
             True,  True,  True,
             True,  True,  True,
             True,  True,  True,
        ])
        self.assertEquals(King(0, 0).territory(Board(3, 3)), [
             True,  True, False,
             True,  True, False,
            False, False, False,
        ])
        self.assertEquals(King(1, 0).territory(Board(3, 3)), [
             True,  True,  True,
             True,  True,  True,
            False, False, False,
        ])
        self.assertEquals(King(2, 0).territory(Board(3, 3)), [
            False,  True,  True,
            False,  True,  True,
            False, False, False,
        ])
        self.assertEquals(King(2, 1).territory(Board(3, 3)), [
            False,  True,  True,
            False,  True,  True,
            False,  True,  True,
        ])
        self.assertEquals(King(2, 2).territory(Board(3, 3)), [
            False, False, False,
            False,  True,  True,
            False,  True,  True,
        ])
        self.assertEquals(King(1, 2).territory(Board(3, 3)), [
            False, False, False,
             True,  True,  True,
             True,  True,  True,
        ])
        self.assertEquals(King(0, 2).territory(Board(3, 3)), [
            False, False, False,
             True,  True, False,
             True,  True, False,
        ])
