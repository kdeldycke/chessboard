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
    division, print_function, absolute_import
)

import time

from bprofile import BProfile
import click
from click.exceptions import BadParameter

from . import __version__, PIECE_LABELS, SolverContext


class PositiveInt(click.types.IntParamType):

    def __init__(self, allow_zero=True):
        self.allow_zero = True

    def convert(self, value, param, ctx):
        """ Like standard int, but check sign and zero. """
        value = super(PositiveInt, self).convert(value, param, ctx)
        if value < 0:
            self.fail('%s is not positive' % value, param, ctx)
        if not self.allow_zero and not value:
            self.fail('%s is not greater than 0' % value, param, ctx)
        return value


POSITIVE_INT = PositiveInt(allow_zero=False)
POSITIVE_OR_ZERO_INT = PositiveInt(allow_zero=True)


class CLI(click.Command):

    def __init__(self, *args, **kwargs):
        """ Override default constructor to add dynamic parameters. """
        for label in PIECE_LABELS:
            kwargs['params'].append(click.Option(
                ('--{}'.format(label), ),
                default=0,
                type=POSITIVE_OR_ZERO_INT,
                help='Number of {}s to add to the board.'.format(label)))
        super(CLI, self).__init__(*args, **kwargs)


@click.command(cls=CLI)
@click.version_option(__version__)
@click.option('-l', '--length', required=True, type=POSITIVE_INT,
              help='Length of the board.')
@click.option('-h', '--height', required=True, type=POSITIVE_INT,
              help='Height of the board.')
@click.option('-s', '--silent', is_flag=True, default=False,
              help='Do not display result board, only final count.')
@click.option('-v', '--verbose', is_flag=True, default=False,
              help='Print much more debug statements.')
@click.option('-p', '--profile', is_flag=True, default=False,
              help='Produce a profiling graph.')
def cli(length, height, silent, verbose, profile, **pieces):
    """ Python CLI to explore chessboard positions. """
    # Check that at least one piece is provided.
    if not sum(pieces.values()):
        context = click.get_current_context()
        raise BadParameter('No piece provided.', ctx=context, param_hint=[
            '--{}'.format(label) for label in PIECE_LABELS])

    # Setup the optionnal profiler.
    profiler = BProfile('solver-profile.png', enabled=profile)

    click.echo('Building up a chessboard...')
    solver = SolverContext(length, height, **pieces)

    click.echo('Searching positions...')
    with profiler:
        start = time.time()
        for result in solver.solve():
            if not silent:
                click.echo(u'{}'.format(result))
        processing_time = time.time() - start

    click.echo('{} results found in {:.2f} seconds.'.format(
        solver.result_counter, processing_time))

    if profile:
        click.echo('Execution profile saved at {}'.format(
            profiler.output_path))
