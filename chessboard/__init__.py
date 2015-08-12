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


__version__ = '0.5.0.dev'


# Defines custom exception first to avoid circular imports.

class ForbiddenPosition(Exception):
    """ Raised when a 2D (x, y) position is out of board's bounds. """


class ForbiddenIndex(Exception):
    """ Raised when a linear index of a square is out of board's bounds. """


class OccupiedPosition(Exception):
    """ Raised when we try to add a piece to an occupied position. """


# Expose important classes to the root of the module.
from pieces import Piece, King, Queen
from chessboard import Chessboard, Board
