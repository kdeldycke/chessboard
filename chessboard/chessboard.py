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
from itertools import chain, combinations
from functools import partial
from operator import and_, or_, truth

from chessboard import (
    ForbiddenIndex,
    ForbiddenCoordinates,
    OccupiedPosition,
    VulnerablePosition,
    AttackablePiece,
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
        'rook',
        'bishop',
        'knight',
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
        self.result_counter = 0
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

    def grouped_permutations(self):
        """ Return unique permutations of linear index grouped by pieces kind.
        """
        perms = []
        for kind, quantity in self.pieces.items():
            if quantity <= 0:
                continue
            perms.append(map(partial(zip, [kind] * quantity), combinations(
                self.vector_indexes, quantity)))
        return perms

    @classmethod
    def tree(cls, level, *sub_levels):
        """ Iterative cartesian product of level sets.

        Depth-first, tree-traversal of the product space.
        """
        for positions in level:
            if sub_levels:
                for sub_positions in cls.tree(*sub_levels):
                    yield chain(positions, sub_positions)
            else:
                yield positions

    def solve(self):
        """ Solve all possible positions of pieces. """
        # Start solving the board.
        start = time.time()

        # Iterate through all combinations of positions.
        for pieces_set in self.tree(*self.grouped_permutations()):

            # Create a new, empty board.
            board = Board(self.length, self.height)

            try:
                for piece_kind, index_position in pieces_set:
                    # Translate linear index to 2D dimension.
                    x, y = board.index_to_coordinates(index_position)
                    # Try to place the piece on the board.
                    board.add(piece_kind, x, y)
            # If one of the piece can't be added, throw the whole set and
            # proceed to the next.
            except (OccupiedPosition, VulnerablePosition, AttackablePiece):
                continue

            # All pieces fits, save solution and proceeed to next permutation.
            self.result_counter += 1
            self.processing_time = time.time() - start
            yield board


class Board(object):
    """ Chessboard of arbitrary dimensions with placed pieces.

    This kind of chessboard only accept new pieces which are not overlapping
    squares:
        * occupied by another piece;
        * directly reachable by another piece.

    Internal states of the board is materialized by a vector. A vector is a
    simple list of boolean for which each element represent a square.
    """

    def __init__(self, length, height):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)
        assert self.length > 0
        assert self.height > 0

        # Store positionned pieces on the board.
        self.pieces = []

        # Squares on the board already occupied by a piece.
        self.occupancy = self.new_vector()

        # Territory susceptible to attacke, i.e. squares reachable by at least
        # a piece,
        self.exposed_territory = self.new_vector()

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Board: length={}, height={}, size={}, pieces={}>'.format(
            self.length, self.height, self.size, self.pieces)

    def __str__(self):
        """ Render the board with pieces in Unicode-art. """
        lines = []

        # Draw top line.
        lines.append((('┬───' * self.length) + '┐').replace('┬', '┌', 1))

        # Draw each line.
        for y in range(self.height):

            # Draw line with the pieces.
            l = ''
            for x in range(self.length):
                piece = self.get(x, y)
                l += '│ {} '.format(piece.symbol if piece else ' ')
            lines.append(l + '│')

            # Draw line separator but the last one.
            if y < (self.height -1):
                lines.append(
                    (('┼───' * self.length) + '┤').replace('┼', '├', 1))

        # Draw bottom line.
        lines.append((('┴───' * self.length) + '┘').replace('┴', '└', 1))

        return '\n'.join(lines)

    @property
    def size(self):
        """ Return the number of squares in the board. """
        return self.length * self.height

    @property
    def indexes(self):
        """ Returns an ordered list of linear indexes of all squares. """
        return range(self.size)

    @property
    def positions(self):
        """ Generator producing all 2D positions of all squares. """
        for y in range(self.height):
            for x in range(self.length):
                yield x, y

    def new_vector(self):
        """ Returns a list of boolean flags of squares indexed linearly.

        All states are initialized to False.
        """
        return [False] * self.size

    def validate_index(self, index):
        """ Check that a linear index of a square is within board's bounds. """
        if index < 0 or index >= self.size:
            raise ForbiddenIndex("Linear index {} not in {}x{} board.".format(
                index, self.length, self.height))

    def validate_coordinates(self, x, y):
        """ Check if the piece lie within the board. """
        if not(x >= 0 and x < self.length and y >= 0 and y < self.height):
            raise ForbiddenCoordinates(
                "x={}, y={} outside of {}x{} board.".format(
                    x, y, self.length, self.height))

    def index_to_coordinates(self, index):
        """ Return a set of 2D (x, y) coordinates from a linear index. """
        self.validate_index(index)
        x = int(index % self.length)
        y = int((index - x) / self.length)
        return x, y

    def coordinates_to_index(self, x, y, x_shift=0, y_shift=0):
        """ Return a linear index from a set of 2D coordinates.

        Optionnal vertical and horizontal shifts might be applied.
        """
        target_x = x + x_shift
        target_y = y + y_shift
        self.validate_coordinates(target_x, target_y)
        index = (target_y * self.length) + target_x
        return index

    def add(self, piece_kind, x, y):
        """ Add a piece to the board. """
        # Create a new instance of the piece.
        klass_name = piece_kind.title()
        klass = getattr(piece_module, klass_name)
        assert issubclass(klass, Piece)
        piece = klass(self, x, y)

        # Try to place the piece on the board.
        index = piece.index

        # Square already occupied by another piece.
        if self.occupancy[index]:
            raise OccupiedPosition

        # Square reachable by another piece.
        if self.exposed_territory[index]:
            raise VulnerablePosition

        # Check if a piece can attack another one from its position.
        territory = piece.territory
        if filter(truth, map(and_, self.occupancy, territory)):
            raise AttackablePiece

        # Mark the piece's territory as vulnerable and secure its position on
        # the board.
        self.pieces.append(piece)
        self.occupancy[piece.index] = True
        self.exposed_territory = map(or_, self.exposed_territory, territory)

    def get(self, x, y):
        """ Return piece placed at the provided coordinates. """
        for piece in self.pieces:
            if (piece.x, piece.y) == (x, y):
                return piece
