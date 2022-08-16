#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ArviZ documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 11 18:33:59 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from typing import Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import arviz

arviz.rcParams["data.load"] = "eager"
arviz.Numba.disable_numba()

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath("../sphinxext"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "matplotlib.sphinxext.plot_directive",
    "bokeh.sphinxext.bokeh_plot",
    "numpydoc",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "gallery_generator",
    "myst_nb",
    "sphinx_design",
    "notfound.extension",
    "sphinx_copybutton",
    "sphinx_codeautolink",
    "jupyter_sphinx",
]

# codeautolink
codeautolink_autodoc_inject = False
codeautolink_search_css_classes = ["highlight-default"]
codeautolink_concat_default = True

# ipython directive configuration
ipython_warning_is_error = False

# Copy plot options from Seaborn
# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False

# Generate API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../_templates"]
#

# MyST related params
nb_execution_mode = "auto"
nb_execution_excludepatterns = ["*.ipynb"]
nb_kernel_rgx_aliases = {".*": "python3"}
myst_heading_anchors = None
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath"]

# copybutton config: strip console characters
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# The base toctree document.
master_doc = "index"
default_role = "code"
suppress_warnings = ["mystnb.unknown_mime_type"]

# General information about the project.
project = "ArviZ"
copyright = "2018, ArviZ devs"
author = "ArviZ devs"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
version = arviz.__version__
if os.environ.get("READTHEDOCS", False):
    rtd_version = os.environ.get("READTHEDOCS_VERSION", "")
    if "." not in rtd_version and rtd_version.lower() != "stable":
        version = "dev"
else:
    branch_name = os.environ.get("BUILD_SOURCEBRANCHNAME", "")
    if branch_name == "main":
        version = "dev"

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "build", "Thumbs.db", ".DS_Store", "notebooks/.ipynb_checkpoints"]
# configure notfound extension to not add any prefix to the urls
notfound_urls_prefix = "/en/latest/"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/arviz-devs/arviz",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/arviz_devs",
            "icon": "fab fa-twitter-square",
        },
    ],
    "navbar_start": ["navbar-logo", "navbar-version"],
    "page_sidebar_items": ["page-toc", "edit-this-page", "donate"],
    "use_edit_page_button": True,
    "google_analytics_id": "G-W1G68W77YV",
    "external_links": [
        {"name": "About", "url": "https://www.arviz.org"},
    ],
}
html_context = {
    "github_user": "arviz-devs",
    "github_repo": "arviz",
    "github_version": "main",
    "doc_path": "doc/source/",
    "default_mode": "light",
}
html_sidebars: Dict[str, Any] = {
    "index": [],
    "community": ["search-field.html", "sidebar-nav-bs.html", "twitter.html"],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# use additional pages to add a 404 page
html_additional_pages = {
    "404": "404.html",
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "ArviZdoc"


# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "ArviZ"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo.png"


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# -- Options for LaTeX output ---------------------------------------------

latex_elements: Dict[str, str] = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "ArviZ.tex", "ArviZ Documentation", "ArviZ devs", "manual")]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "arviz", "ArviZ Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "ArviZ",
        "ArviZ Documentation",
        author,
        "ArviZ",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# Example configuration for intersphinx
intersphinx_mapping = {
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    # Oriol: I am lazy and didn't want to update any references we might have using the pymc3 key
    "pymc3": ("https://www.pymc.io/projects/docs/en/stable", None),
    "pymc": ("https://www.pymc.io/projects/docs/en/stable", None),
    "mpl": ("https://matplotlib.org/stable", None),
    "bokeh": ("https://docs.bokeh.org/en/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "zarr": ("https://zarr.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "dask": ("https://docs.dask.org/en/latest/", None),
    "sphinx-primer": ("https://sphinx-primer.readthedocs.io/en/latest/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "diataxis": ("https://diataxis.fr/", None),
    "arviz_org": ("https://www.arviz.org/en/latest/", None),
}


def setup(app):
    # this needs to be added so we can reference confval targets
    # in the doc contributing pages and explain what values we use and why
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
