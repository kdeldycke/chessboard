# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import os
import sys
import time

# Expose package to autodoc.
sys.path.insert(0, os.path.abspath('..'))
import chessboard

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

master_doc = 'index'

project = "Chessboard"
author = "Kevin Deldycke"

# We use our own copyright template instead of the default as the latter strip
# HTML content.
html_show_copyright = False
copyright = "2015-{}, <a href='http://kevin.deldycke.com'>{}</a>".format(
    time.strftime('%Y'), author)

version = release = chessboard.__version__

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

nitpicky = True
# We need a recent sphinx because of the last update format.
needs_sphinx = '1.4'
html_last_updated_fmt = 'YYYY-MM-dd'
templates_path = ['templates']

# Enforce Google style docstrings.
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Use readthedocs.org theme both locally and online.
# Source: https://github.com/snide/sphinx_rtd_theme#using-this-theme-locally-then-building-on-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

htmlhelp_basename = project
