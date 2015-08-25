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

""" Definition of chess pieces and their behavioural properties. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

from itertools import chain, izip_longest

from chessboard import ForbiddenCoordinates


class Piece(object):
    """ A generic piece.

    x: horizontal position of the piece.
    y: vertical position of the piece.
    """

    def __init__(self, board, index):
        """ Place the piece on a board at the provided linear position. """
        self.board = board
        self.index = index
        self.x, self.y = self.board.index_to_coordinates(self.index)

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<{}: x={}, y={}; index={}>'.format(
            self.__class__.__name__, self.x, self.y, self.index)

    @property
    def bottom_distance(self):
        """ Number of squares separating the piece from the bottom of the board.
        """
        return self.board.height - 1 - self.y

    @property
    def right_distance(self):
        """ Number of squares separating the piece from the right of the board.
        """
        return self.board.length - 1 - self.x

    @property
    def top_distance(self):
        """ Number of squares separating the piece from the top of the board.
        """
        return self.y

    @property
    def left_distance(self):
        """ Number of squares separating the piece from the left of the board.
        """
        return self.x

    @property
    def horizontals(self):
        """ All horizontal squares from the piece's point of view.

        Returns a list of relative movements up to the board's bound.
        """
        horizontal_shifts = set(izip_longest(map(
            lambda i: i - self.x, range(self.board.length)), [], fillvalue=0))
        horizontal_shifts.discard((0, 0))
        return horizontal_shifts

    @property
    def verticals(self):
        """ All vertical squares from the piece's point of view.

        Returns a list of relative movements up to the board's bound.
        """
        vertical_shifts = set(izip_longest([], map(
            lambda i: i - self.y, range(self.board.height)), fillvalue=0))
        vertical_shifts.discard((0, 0))
        return vertical_shifts

    @property
    def diagonals(self):
        """ All diagonal squares from the piece's point of view.

        Returns a list of relative movements up to the board's bound.
        """
        left_top_shifts = map(lambda i: (-(i+1), -(i+1)), range(min(
            self.left_distance, self.top_distance)))
        left_bottom_shifts = map(lambda i: (-(i+1), +(i+1)), range(min(
            self.left_distance, self.bottom_distance)))
        right_top_shifts = map(lambda i: (+(i+1), -(i+1)), range(min(
            self.right_distance, self.top_distance)))
        right_bottom_shifts = map(lambda i: (+(i+1), +(i+1)), range(min(
            self.right_distance, self.bottom_distance)))
        return set(chain(
            left_top_shifts, left_bottom_shifts,
            right_top_shifts, right_bottom_shifts))

    @property
    def movements(self):
        """ Return list of relative movements allowed. """
        raise NotImplementedError

    @property
    def territory(self):
        """ Territory reachable by the piece from its current position.

        Returns a list of boolean flags of squares indexed linearly, for which
        a True means the square is reachable.
        """
        # Initialize the square occupancy vector of the board.
        vector = self.board.new_vector()

        # Mark current position as reachable.
        vector[self.index] = True

        # List all places reacheable by the piece from its current position.
        for x_shift, y_shift in self.movements:
            # Mark side positions as reachable if in the limit of the board.
            try:
                reachable_index = self.board.coordinates_to_index(
                    self.x, self.y, x_shift, y_shift)
            except ForbiddenCoordinates:
                continue
            vector[reachable_index] = True

        return vector


class King(Piece):
    """ King model. """

    symbol = '♚'

    @property
    def movements(self):
        """ King moves one square in any direction.

        Don't mind out-of-bounds relative positions: forbidden ones will be
        silently discarded within the ``Piece.territory()`` method above.
        """
        return set([
            # Horizontal movements.
            (+1, 0), (-1, 0),
            # Vertical movements.
            (0, +1), (0, -1),
            # Diagonal movements.
            (+1, +1), (-1, -1), (-1, +1), (+1, -1),
        ])


class Queen(Piece):
    """ Queen model. """

    symbol = '♛'

    @property
    def movements(self):
        """ Queen moves unrestricted horizontally, vertically and diagonally.
        """
        return self.horizontals | self.verticals | self.diagonals


class Rook(Piece):
    """ Rook model. """

    symbol = '♜'

    @property
    def movements(self):
        """ Rook moves unrestricted horizontally and vertically. """
        return self.horizontals | self.verticals


class Bishop(Piece):
    """ Bishop model. """

    symbol = '♝'

    @property
    def movements(self):
        """ Bishop moves unrestricted diagonally. """
        return self.diagonals


class Knight(Piece):
    """ Knight model. """

    symbol = '♞'

    @property
    def movements(self):
        """ Knight moves in L shapes in all 8 directions.

        Don't mind out-of-bounds relative positions: forbidden ones will be
        silently discarded within the ``Piece.territory()`` method above.
        """
        return set([
            # Top-right movements.
            (+2, +1), (+1, +2),
            # Top-left movements.
            (-2, +1), (-1, +2),
            # Bottom-right movements.
            (+2, -1), (+1, -2),
            # Bottom-left movements.
            (-2, -1), (-1, -2),
        ])
