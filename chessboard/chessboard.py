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

""" Chessboard objects and utilities.

2D positions on the board are noted (x, y).

The horizontal range x goes from 0 to m-1.
The vertical range y goes from 0 to n-1.

The top-left position is (0, 0).
The top-right position is (0, m-1).
The bottom-left position is (n-1, 0).
The bottom-right position is (n-1, m-1).

          0 1 2 3 4 ...
        0 . . . . .
        1 . . . . .
        2 . . . . .
        3 . . . . .
        4 . . . . .
        ...

"""

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

#https://news.ycombinator.com/item?id=10028742

import time
from itertools import chain, permutations
from operator import and_, or_

from chessboard import (
    ForbiddenIndex,
    OccupiedPosition,
    Piece,
    pieces as piece_module
)


class Chessboard(object):
    """ Initialize a chessboard context.

    TODO: This initialization code belongs to the CLI domain really.

    TODO: or rename to solver instead.
    """

    # List of recognized pieces.
    PIECE_TYPES = frozenset([
        'king',
        'queen',
        #'bishop',
        #'rook',
        #'knight'
    ])

    def __init__(self, length, height, **pieces):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)
        assert self.length > 0
        assert self.height > 0

        # Store the number of pieces on the board.
        self.pieces = {}
        for kind, quantity in pieces.items():
            assert kind in self.PIECE_TYPES
            assert isinstance(quantity, int)
            assert quantity >= 0
            self.pieces[kind] = quantity

        # Solver metadata.
        self.processing_time = None

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Chessboard: length={}, height={}, pieces={}>'.format(
            self.length, self.height, self.pieces)

    @property
    def vector_size(self):
        return self.length * self.height

    @property
    def vector_indexes(self):
        return range(self.vector_size)

    def permutations(self):
        """ Returns unique permutations of piece types and linear positions.

        TODO: Refactor to a pure unique iterator.
        TODO: use symetries to reduce the search space.
        """
        # Use a set to deduplicate permutations.
        unique_perms = set()

        # Serialize and freeze pieces index by kind.
        pieces = list(chain(*[
            [kind] * quantity for kind, quantity in self.pieces.items()]))

        # Iterate all permutations of pieces over all linear positions of the
        # board.
        for positions in permutations(self.vector_indexes, len(pieces)):
            unique_perms.add(frozenset(zip(pieces, positions)))

        return unique_perms

    def solve(self):
        """ Solve all possible positions of pieces.

        Use a stupid brute-force approach for now.

        TODO: Use a binary search to exlude whole branches as soon as possible.
        """
        results = []

        # Start solving the board.
        start = time.time()

        # Try all permutations of available pieces within the board vector.
        for pieces_set in self.permutations():

            # Create a new, empty board.
            board = Board(self.length, self.height)

            try:
                for piece_kind, linear_position in pieces_set:
                    # Translate linear index to 2D dimension.
                    x, y = board.linear_position(linear_position)
                    # Try to place the piece on the board.
                    board.add(piece_kind, x, y)
            # If one of the piece can't be added because the territory is
            # already occupied, throw the whole set and proceed to the next.
            except OccupiedPosition:
                continue

            # All pieces fits, save solution and proceeed to next permutation.
            results.append(board)

        self.processing_time = time.time() - start

        return results


class Board(object):
    """ Chessboard of arbitrary dimensions with placed pieces.

    This kind of chessboard only accept new pieces which are not overlapping
    squares:
        * occupied by another piece;
        * directly reachable by another piece.
    """

    def __init__(self, length, height):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)
        assert self.length > 0
        assert self.height > 0

        # Initialize board states. This is a linear list of bolean flags
        # indicating if a square on the board is available or not.
        self.square_occupancy = [False] * self.size

        # Store positionned pieces on the board.
        self.pieces = []

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Board: length={}, height={}, size={}, pieces={}>'.format(
            self.length, self.height, self.size, self.pieces)

    def all_positions(self):
        """ Generator producing all positions. """
        for x in range(0, self.length - 1):
            for y in range(0, self.height - 1):
                yield x, y

    @property
    def size(self):
        return self.length * self.height

    @property
    def indexes(self):
        """ Returns an ordered list of linear indexes of all squares. """
        return range(self.size)

    def validate_index(self, index):
        """ Checks that a linear index of a square is within board's bounds.
        """
        if index < 0 or index >= self.size:
            raise ForbiddenIndex("Linear index {} not in {}x{} board.".format(
                index, self.length, self.height))

    def linear_position(self, index):
        """ Returns a set of 2D (x, y) coordinates from a linear index. """
        self.validate_index(index)
        x = int(index % self.length)
        y = int((index - x) / self.height)
        return x, y

    def add(self, piece_kind, x, y):
        """ Add a piece to the board. """
        # Create a new instance of the piece.
        klass_name = piece_kind.title()
        klass = getattr(piece_module, klass_name)
        assert issubclass(klass, Piece)
        piece = klass(self, x, y)

        # Get piece's occupied and reachable territory in the context of the
        # board.
        territory = piece.territory

        # Check that the piece's territory doesn't overlap the territory
        # already reserved by other pieces.
        overlap = filter(
            lambda square: square is True,
            map(and_, self.square_occupancy, territory))
        if overlap:
            raise OccupiedPosition

        # Mark the piece's territory as no longer available.
        self.pieces.append(piece)
        self.square_occupancy = map(or_, self.square_occupancy, territory)
