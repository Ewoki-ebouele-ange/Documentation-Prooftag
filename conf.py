# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Prooftag Doc's"
copyright = '2023, Prooftag auth'
author = 'Prooftag auth'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Dans le fichier conf.py, spécifiez le bon répertoire de sortie
import os

# Utilisez le répertoire de sortie standard de Read the Docs
output_dir = os.getenv('READTHEDOCS_OUTPUT', default='_build/html')

# Configurez le répertoire de sortie pour la documentation générée
html_context = {
    'output_dir': output_dir,
}