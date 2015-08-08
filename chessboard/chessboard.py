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

import logging


class Chessboard(object):
    """ Model representing a chessboard of arbitrary dimensions. """

    # Restrict dimension since we haven't benchmarked the perforances yet.
    MAX_DIMENSION = 3

    def __init__(self, length, height):
        self.length = length
        self.height = height
        assert isinstance(self.length, int)
        assert isinstance(self.height, int)

    def __repr__(self):
        return '<Chessboard: length={}, height={}>'.format(
            self.length, self.height)
