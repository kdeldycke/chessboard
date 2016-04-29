# -*- coding: utf-8 -*-

import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Chessboard'
copyright = u'2016, Kevin Deldycke'
author = u'Kevin Deldycke'

version = u'1.5.0'
release = u'1.5.0'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Append '()' to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Use readthedocs.org theme both locally and online.
# Source: https://github.com/snide/sphinx_rtd_theme#using-this-theme-locally-then-building-on-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

htmlhelp_basename = 'Chessboarddoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
