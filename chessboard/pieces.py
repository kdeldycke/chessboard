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


class Piece(object):
    """ A generic piece.

    x: horizontal position of the piece.
    y: vertical position of the piece.
    """

    def __init__(self, board, x, y):
        """ Place the piece at the (x, y) coordinates of the provided board.
        """
        self.x = x
        self.y = y
        self.board = board

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<{}: x={}, y={}>'.format(
            self.__class__.__name__, self.x, self.y)

    def bottom_distance(self):
        """ Number of squares separating the piece from the bottom of the board.
        """
        return self.board.height - 1 - self.y

    def right_distance(self):
        """ Number of squares separating the piece from the right of the board.
        """
        return self.board.length - 1 - self.x

    def top_distance(self):
        """ Number of squares separating the piece from the top of the board.
        """
        return self.y

    def left_distance(self):
        """ Number of squares separating the piece from the left of the board.
        """
        return self.x

    def translate(self, x_shift=0, y_shift=0):
        """ Translate 2D coordinates to vector index. """
        target_x = self.x + x_shift
        target_y = self.y + y_shift
        self.board.validate_position(target_x, target_y)
        vector_index = (target_y * self.board.length) + target_x
        return vector_index

    def movements(self):
        """ Return list of relative movements allowed. """
        raise NotImplementedError

    def territory(self):
        """ given a position on the checkboard, give a vector
        of places the king is allowed to occupy.

        x: horizontal position of the king
        y: vertical position of the king
        """
        # Initialize the square occupancy vector of the board.
        vector = [False] * self.board.length * self.board.height

        # Translate (x, y) coordinates to linear position.
        current_position = (self.y * self.board.length) + self.x

        # Mark current position as occupied.
        vector[current_position] = True

        # List all places reacheable by the piece from its current position.
        for x_shift, y_shift in self.movements():
            # Mark side positions as reachable if in the limit of the board.
            try:
                target_position = self.translate(x_shift, y_shift)
            except ValueError:
                continue
            vector[target_position] = True

        return vector


class King(Piece):
    """ King model. """

    def movements(self):
        """ King moves one square in any direction. """
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

    def movements(self):
        """ Queen moves unrestricted vertically, horizontally and diagonally.
        """
        horizontal_shifts = izip_longest(map(
            lambda i: i - self.x, range(self.board.length)), [], fillvalue=0)

        vertical_shifts = izip_longest([], map(
            lambda i: i - self.y, range(self.board.height)), fillvalue=0)

        left_top_shifts = map(lambda i: (-(i+1), -(i+1)), range(min(
            self.left_distance(), self.top_distance())))
        left_bottom_shifts = map(lambda i: (-(i+1), +(i+1)), range(min(
            self.left_distance(), self.bottom_distance())))
        right_top_shifts = map(lambda i: (+(i+1), -(i+1)), range(min(
            self.right_distance(), self.top_distance())))
        right_bottom_shifts = map(lambda i: (+(i+1), +(i+1)), range(min(
            self.right_distance(), self.bottom_distance())))

        shifts = set(chain(
            horizontal_shifts, vertical_shifts,
            left_top_shifts, left_bottom_shifts,
            right_top_shifts, right_bottom_shifts,
        ))

        shifts.discard((0, 0))

        return shifts
