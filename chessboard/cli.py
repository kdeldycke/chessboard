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

from __future__ import absolute_import, division, print_function

import multiprocessing
import time

import click
from click.exceptions import BadParameter

import click_log
from bprofile import BProfile
from chessboard.benchmark import run_scenario

from . import PIECE_LABELS, Benchmark, SolverContext, __version__, logger


class PositiveInt(click.types.IntParamType):
    """ Custom type class for click to validate positive integers. """

    def __init__(self, allow_zero=True):
        """ Validator can be customized to consider 0 as allowed or not. """
        self.allow_zero = allow_zero

    def convert(self, value, param, ctx):
        """ Reuse standard integer validator but add checks on sign and zero.
        """
        value = super(PositiveInt, self).convert(value, param, ctx)
        if value < 0:
            self.fail('%s is not positive' % value, param, ctx)
        if not self.allow_zero and not value:
            self.fail('%s is not greater than 0' % value, param, ctx)
        return value


# Shortcut to pre-configured validators.
POSITIVE_INT = PositiveInt(allow_zero=False)
POSITIVE_OR_ZERO_INT = PositiveInt(allow_zero=True)


class Solve(click.Command):
    """ Manage the solve command. """

    def __init__(self, *args, **kwargs):
        """ Override default constructor to dynamiccaly add pieces options. """
        for label in PIECE_LABELS:
            kwargs['params'].append(click.Option(
                ('--{}'.format(label), ),
                default=0,
                type=POSITIVE_OR_ZERO_INT,
                help='Number of {}s.'.format(label)))
        super(Solve, self).__init__(*args, **kwargs)


@click.group(invoke_without_command=True)
@click_log.init(logger)
@click_log.simple_verbosity_option(
    default='INFO', metavar='LEVEL',
    help='Either CRITICAL, ERROR, WARNING, INFO or DEBUG. Defaults to INFO.')
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    """ CLI to solve combinatoric chess puzzles. """
    # Print help screen and exit if no sub-commands provided.
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command(cls=Solve, short_help='Solve a chess puzzle.')
@click.option(
    '-l', '--length', required=True, type=POSITIVE_INT,
    help='Length of the board.')
@click.option(
    '-h', '--height', required=True, type=POSITIVE_INT,
    help='Height of the board.')
@click.option(
    '-s', '--silent', is_flag=True, default=False,
    help='Do not render result boards in ASCII-art.')
@click.option(
    '-p', '--profile', is_flag=True, default=False,
    help='Produce a profiling graph.')
@click.pass_context
def solve(ctx, length, height, silent, profile, **pieces):
    """ Solve a puzzle constrained by board dimensions and pieces. """
    # Check that at least one piece is provided.
    if not sum(pieces.values()):
        context = click.get_current_context()
        raise BadParameter('No piece provided.', ctx=context, param_hint=[
            '--{}'.format(label) for label in PIECE_LABELS])

    # Setup the optionnal profiler.
    profiler = BProfile('solver-profile.png', enabled=profile)

    solver = SolverContext(length, height, **pieces)
    logger.info(repr(solver))

    logger.info('Searching positions...')
    with profiler:
        start = time.time()
        for result in solver.solve():
            if not silent:
                click.echo(u'{}'.format(result))
        processing_time = time.time() - start

    logger.info('{} results found in {:.2f} seconds.'.format(
        solver.result_counter, processing_time))

    if profile:
        logger.info('Execution profile saved at {}'.format(
            profiler.output_path))


@cli.command(short_help='Benchmark the solver.')
def benchmark():
    """ Run a benchmarking suite and measure time taken by the solver.

    Each scenario is run in an isolated process, and results are appended to
    CSV file.
    """
    # Use all cores but one on multi-core CPUs.
    pool_size = multiprocessing.cpu_count() - 1
    if pool_size < 1:
        pool_size = 1

    # Start a pool of workers. Only allow 1 task per child, to force flushing
    # of solver's internal caches.
    pool = multiprocessing.Pool(processes=pool_size, maxtasksperchild=1)
    results = pool.imap_unordered(run_scenario, Benchmark.scenarii)
    pool.close()
    pool.join()

    # Update CSV database with the new results.
    benchmark = Benchmark()
    benchmark.load_csv()
    benchmark.add(results)
    benchmark.save_csv()


@cli.command(short_help='Plot solver performances.')
def graph():
    """ Update all kind of performance graphs from the benchmark data.

    All data come from CSV database.
    """
    benchmark = Benchmark()
    benchmark.load_csv()
    benchmark.nqueen_graph()
