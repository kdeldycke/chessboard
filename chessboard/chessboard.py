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

""" Chessboard objects and utilities. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import time
import logging


class Chessboard(object):
    """ Initialize a chessboard context.

    TODO: This initialization code belongs to the CLI domain really.
    """

    # Restrict dimension since we haven't benchmarked the perforances yet.
    MAX_DIMENSION = 3

    # List of recognized pieces.
    PIECE_TYPES = frozenset([
        'king',
        'queen',
        'bishop',
        'rook',
        'knight'])

    def __init__(self, length, height, **pieces):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)

        # Store the number of pieces on the board.
        self.pieces = dict.fromkeys(self.PIECE_TYPES, 0)
        self.add(**pieces)

        # Solver data.
        processing_time = None

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Chessboard: length={}, height={}, pieces={}>'.format(
            self.length, self.height, self.pieces)

    def add(self, **pieces):
        """ Add an arbitrary number of pieces to the board. """
        for piece_type, quantity in pieces.items():
            assert piece_type in self.PIECE_TYPES
            assert isinstance(quantity, int)
            self.pieces[piece_type] += quantity

    def solve(self):
        """ Solve all possible positions of pieces.

        Use a stupid brute-force approach for now.
        """
        results = None

        # Start solving the board.
        start = time.time()

        # Nope.

        end = time.time()
        self.processing_time = end - start

        return results


class Board(object):
    """ Chessboard of arbitrary dimensions with placed pieces.

    This kind of chessboard only accept new pieces which are not overlapping
    cases of:
        * a piece already occupying the case
        * a case reachable by another piece.
    """

    # Restrict dimension since we haven't benchmarked the perforances yet.
    MAX_DIMENSION = 3

    def __init__(self, length, height):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)
        assert self.MAX_DIMENSION >= self.length > 0
        assert self.MAX_DIMENSION >= self.height > 0

        # Initialize board states. This is a linear list of bolean flags
        # indicating if a case on the board is available or not.
        self.states = [False] * self.length * self.height

        # Store pieces and their position on the board.
        self.pieces = []

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Board: length={}, height={}, pieces={}>'.format(
            self.length, self.height, self.pieces)

    def all_positions(self):
        """ Generator producing all positions. """
        for x in range(0, self.length - 1):
            for y in range(0, self.height - 1):
                yield x, y

    def validate_position(self, x, y):
        """ Check if a 2D position is within the board. """
        if not(x >= 0 and x < self.length and y >= 0 and y < self.height):
            raise ValueError


class King(object):
    """ King model and behavioural properties. """

    # List of relative movements allowed.
    MOVEMENTS = [
        (+1,  0),
        (-1,  0),
        ( 0, +1),
        ( 0, -1)]

    def __init__(self, x, y):
        """ Initialize the piece at the (x, y) coordinates of the board. """
        self.x = x
        self.y = y

    def translate(self, board, x_shift=0, y_shift=0):
        """ Translate 2D coordinates to vector index. """
        target_x = self.x + x_shift
        target_y = self.y + y_shift
        board.validate_position(target_x, target_y)
        vector_index = (target_x * board.length) + target_y
        return vector_index

    def territory(self, board):
        """ given a position on the checkboard, give a vector
        of places the king is allowed to occupy.

        x: horizontal position of the king
        y: vertical position of the king

        m: length of the board.
        n: height of the board.
        """
        # Initialize the state vector of the board.
        vector = [False] * board.length * board.height

        # Translate (x, y) coordinates to linear position.
        current_position = (self.x * board.length) + self.y

        # Mark current position as occupied.
        vector[current_position] = True

        # List all places reacheable by the piece from its current position.
        for x_shift, y_shift in self.MOVEMENTS:
            # Mark side positions as reachable if in the limit of the board.
            try:
                target_position = self.translate(board, x_shift, y_shift)
            except ValueError:
                continue
            vector[target_position] = True

        return vector
