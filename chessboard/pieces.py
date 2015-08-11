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


class Piece(object):
    """ A generic piece. """

    def __init__(self, x, y):
        """ Initialize the piece at the (x, y) coordinates of the board. """
        self.x = x
        self.y = y

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<Piece: x={}, y={}>'.format(self.x, self.y)

    def translate(self, board, x_shift=0, y_shift=0):
        """ Translate 2D coordinates to vector index. """
        target_x = self.x + x_shift
        target_y = self.y + y_shift
        board.validate_position(target_x, target_y)
        vector_index = (target_y * board.length) + target_x
        return vector_index

    @classmethod
    def movements(cls):
        """ Return list of relative movements allowed. """
        raise NotImplementedError

    def territory(self, board):
        """ given a position on the checkboard, give a vector
        of places the king is allowed to occupy.

        x: horizontal position of the king
        y: vertical position of the king
        """
        # Initialize the state vector of the board.
        vector = [False] * board.length * board.height

        # Translate (x, y) coordinates to linear position.
        current_position = (self.y * board.length) + self.x

        # Mark current position as occupied.
        vector[current_position] = True

        # List all places reacheable by the piece from its current position.
        for x_shift, y_shift in self.movements():
            # Mark side positions as reachable if in the limit of the board.
            try:
                target_position = self.translate(board, x_shift, y_shift)
            except ValueError:
                continue
            vector[target_position] = True

        return vector


class King(Piece):
    """ King model. """

    @classmethod
    def movements(cls):
        """ A king move up, down and sideways in 1-case increment. """
        return [
            # Horizontal movements.
            (+1, 0), (-1, 0),
            # Vertical movements.
            (0, +1), (0, -1),
            # Diagonal movements.
            (+1, +1), (-1, -1), (-1, +1), (+1, -1),
        ]
