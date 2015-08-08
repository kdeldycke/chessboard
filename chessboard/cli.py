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

from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import logging

import click

from . import __version__
from .chessboard import Chessboard


log = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.version_option(__version__)
@click.option('-l', '--length', default=3, help='Length of the board.')
@click.option('-h', '--height', default=3, help='Height of the board.')
@click.option('-v', '--verbose', is_flag=True, default=False,
              help='Print much more debug statements.')
def cli(length, height, verbose):
    """ Python CLI to explore chessboard positions. """
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    click.echo('Building up a chessboard...')
    board = Chessboard(length, height)

    click.echo('{!r}'.format(board))
