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

""" Board repesentation and utilities. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

from operator import and_, or_, truth

from chessboard import (
    ForbiddenIndex,
    ForbiddenCoordinates,
    OccupiedPosition,
    VulnerablePosition,
    AttackablePiece,
    PIECE_CLASSES,
)


class Board(object):
    """ Chessboard of arbitrary dimensions with placed pieces.

    This kind of chessboard only accept new pieces which are not overlapping
    squares:
        * occupied by another piece;
        * directly reachable by another piece.

    Internal states of the board is materialized by a vector. A vector is a
    simple list of boolean for which each element represent a square.

    2D positions on the board are noted (x, y):
        * horizontal range x goes from 0 to m-1.
        * vertical range y goes from 0 to n-1.
        * top-left position is (0, 0).
        * top-right position is (0, m-1).
        * bottom-left position is (n-1, 0).
        * bottom-right position is (n-1, m-1).

          0 1 2 3 4 …
        0 . . . . .
        1 . . . . .
        2 . . . . .
        3 . . . . .
        4 . . . . .
        …
    """

    def __init__(self, length, height):
        """ Initialize board dimensions. """
        self.length = length
        self.height = height

        # Store positionned pieces on the board.
        self.pieces = []

        # Squares on the board already occupied by a piece.
        self.occupancy = self.new_vector()

        # Territory susceptible to attacke, i.e. squares reachable by at least
        # a piece.
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
            line = ''
            for x in range(self.length):
                piece = self.get(x, y)
                line += '│ {} '.format(piece.symbol if piece else ' ')
            lines.append(line + '│')
            # Draw line separator but the last one.
            if y < (self.height - 1):
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

    def add(self, piece_symbol, index):
        """ Add a piece to the board at the provided linear position. """
        # Square already occupied by another piece.
        if self.occupancy[index]:
            raise OccupiedPosition

        # Square reachable by another piece.
        if self.exposed_territory[index]:
            raise VulnerablePosition

        # Create a new instance of the piece.
        klass = PIECE_CLASSES[piece_symbol]
        piece = klass(self, index)

        # Check if a piece can attack another one from its position.
        territory = piece.territory
        if filter(truth, map(and_, self.occupancy, territory)):
            raise AttackablePiece

        # Mark the territory covered by the piece as exposed and secure its
        # position on the board.
        self.pieces.append(piece)
        self.occupancy[index] = True
        self.exposed_territory = map(or_, self.exposed_territory, territory)

    def get(self, x, y):
        """ Return piece placed at the provided coordinates. """
        for piece in self.pieces:
            if (piece.x, piece.y) == (x, y):
                return piece
