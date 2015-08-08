# -*- coding: utf-8 -*-
from __future__ import (
    division, print_function, absolute_import, unicode_literals
)

import logging

import click

from . import __version__
from .chessboard import Chessboard


log = logging.getLogger(__name__)


@click.group()
@click.version_option(__version__)
@click.option('-v', '--verbose', is_flag=True, default=False,
              help='Print much more debug statements.')
def cli(verbose):
    """ Python CLI to explore chessboard positions. """
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    click.echo('Building up a chessboard...')
    board = Chessboard(length, height)
