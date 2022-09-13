# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Cabrillo Robotics Club'
copyright = '2022, Cabrillo Robotics Club'
author = 'Cabrillo Robotics Club'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxawesome_theme']


templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store',
    'venv*/**',
    '_themes',
    ]

# MyST config.
myst_enable_extensions = ["colon_fence"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'pydata_sphinx_theme'
html_theme = "sphinxawesome_theme"
html_static_path = ['_static']

# This option is `False` by default
html_awesome_docsearch = False

#docsearch_config = {
#  "app_id": "MG8IQJ9KU0",
#  "api_key": "241095237ab6fbc4a644836eab43eb09",
#  "index_name": "cabrillorobotics.org"
#}

#awesome theme config
html_theme_options = {
    "nav_include_hidden": True,
    "show_nav": True,
    "show_breadcrumbs": True,
    "breadcrumbs_separator": "/",
    "show_prev_next": False,
    "show_scrolltop": True
    }

