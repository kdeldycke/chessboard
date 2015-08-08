# -*- coding: utf-8 -*-
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
