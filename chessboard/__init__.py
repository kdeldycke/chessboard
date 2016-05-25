# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2016 Kevin Deldycke <kevin@deldycke.com>
#                         and contributors.
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

""" Expose package-wide elements. """


__version__ = '1.5.0'


import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


# Defines custom exception first to avoid circular imports.

class ForbiddenCoordinates(Exception):

    """ A position given as 2D coordinates are out of board's bounds. """


class ForbiddenIndex(Exception):

    """ A position given as an index is out of board's bounds. """


class OccupiedPosition(Exception):

    """ A piece is added to a position already occupied by another. """


class VulnerablePosition(Exception):

    """ A piece is added to a position reachable by another. """


class AttackablePiece(Exception):

    """ A piece is added to a position from which it can attack another. """


# Expose important classes to the root of the module. These are not
# lexicographically sorted to avoid cyclic imports.
from chessboard.pieces import (
    Piece,
    King, Queen, Rook, Bishop, Knight,
    PIECE_LABELS, PIECE_CLASSES)
from chessboard.board import Board
from chessboard.solver import Permutations, SolverContext
from chessboard.benchmark import Benchmark

import logging

logger = logging.getLogger(__name__)
