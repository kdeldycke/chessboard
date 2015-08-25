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

""" Utilities to search for valid set of positions. """

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

from itertools import chain

from chessboard import (
    AttackablePiece,
    Board,
    OccupiedPosition,
    PIECE_TYPES,
    VulnerablePosition,
)


class Permutations(object):
    """ Produce permutations of piece iteratively. """

    def __init__(self, pieces, range_size=None):
        # Transform the description of pieces population into a linear vector
        # sorted by kind.
        self.pieces = sorted(list(chain(*[
            [kind] * quantity for kind, quantity in pieces.items()])))

        # Maximal depth of the tree.
        self.depth = len(self.pieces)

        # Range of permutations.
        self.range_size = range_size if range_size else self.depth

        # Keep track of our current progression in search space. This variable
        # always holds the last permutation we returned.
        self.indexes = None

    def increment(self):
        """ Increment the last permutation we returned to the next. """
        # Increment position from the deepest place of the tree first.
        for index in reversed(range(self.depth)):
            self.indexes[index] += 1
            # We haven't reach the end of board, no beed to adjust upper level.
            if self.indexes[index] < self.range_size:
                break
            # We've reached the end of board. Reset current level and increment
            # the upper level.
            self.indexes[index] = 0

        # Now that we incremented our indexes, we need to deduplicate positions
        # of the same kind, by aligning piece's indexes to their parents. This
        # works thanks to the sort performed on self.pieces initialization.
        for i in range(self.depth - 1):
            if (self.pieces[i] == self.pieces[i + 1]) and (
                    self.indexes[i] > self.indexes[i + 1]):
                self.indexes[i + 1] = self.indexes[i]

    def __iter__(self):
        return self

    def next(self):
        """ Return next valid permutation.

        Raise iteration exception when we explored all permutations.
        """
        if self.indexes is None:
            self.indexes = [0] * self.depth
        elif self.indexes == [self.range_size - 1] * self.depth:
            raise StopIteration
        else:
            self.increment()
        return zip(self.pieces, self.indexes)

    def skip_branch(self, level):
        """ Abandon the branch at the provided level and skip to the next.

        When we call out to skip to the next branch of the search space, we
        push sublevel pieces to the maximum positions of the board. So that the
        next time the permutation iterator is called, it can produce the vector
        state of the next adjacent branch.
        """
        for i in range(level + 1, self.depth):
            self.indexes[i] = self.range_size - 1


class SolverContext(object):
    """ Initialize a chessboard context and search for all possible positions.

    The search space is constrained by board dimensions and piece population.
    """

    def __init__(self, length, height, **pieces):
        """ Initialize board dimensions and piece population."""
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)
        assert self.length > 0
        assert self.height > 0

        # Store the number of pieces on the board.
        self.pieces = {}
        for kind, quantity in pieces.items():
            assert kind in PIECE_TYPES
            assert isinstance(quantity, int)
            assert quantity >= 0
            self.pieces[kind] = quantity
        assert sum(self.pieces.values()) > 0

        # Solver metadata.
        self.result_counter = 0

    def __repr__(self):
        """ Display all relevant object internals. """
        return '<SolverContext: length={}, height={}, pieces={}>'.format(
            self.length, self.height, self.pieces)

    @property
    def vector_size(self):
        return self.length * self.height

    @property
    def vector_indexes(self):
        return range(self.vector_size)

    def solve(self):
        """ Solve all possible positions of pieces within the context.

        Depth-first, tree-traversal of the product space.
        """
        permutations = Permutations(self.pieces, self.vector_size)

        # Iterate through all combinations of positions.
        for positions in permutations:

            # Create a new, empty board.
            board = Board(self.length, self.height)

            for level, (piece_kind, linear_position) in enumerate(positions):
                # Try to place the piece on the board.
                try:
                    board.add(piece_kind, linear_position)
                # If one of the piece can't be added, throw the whole set, skip
                # the rotten branch and proceed to the next.
                except (OccupiedPosition, VulnerablePosition, AttackablePiece):
                    permutations.skip_branch(level)
                    break

            else:
                # All pieces fits, save solution and proceeed to the next
                # permutation.
                self.result_counter += 1
                yield board
