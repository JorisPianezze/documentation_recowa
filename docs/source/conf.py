# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        Configuration file for the Sphinx documentation builder.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -- Project information -----------------------------------------------------

project   = 'RECOWA'
copyright = '2026, J. Pianezze'
author    = 'J. Pianezze'
release   = '0.0'
version   = '0.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.mermaid',
    'sphinx_substitution_extensions',
    'sphinx_treeview',
    'sphinx_togglebutton',
    'sphinx_design',
    'myst_parser'
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

bibtex_bibfiles        = ['references.bib']
bibtex_default_style   = 'unsrt'
bibtex_reference_style = 'author_year'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
