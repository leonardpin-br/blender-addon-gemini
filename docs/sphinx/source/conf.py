# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../../../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Gimini Blender Addon'
copyright = "2024, Leonardo Pinheiro (based on ST3's work)"
author = "Leonardo Pinheiro (based on ST3's work)"
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc'
]

autodoc_mock_imports = [
    'bgl',
    'blf',
    'bpy',
    'bpy_extras',
    'gpu',
    'gpu_extras',
    'mathutils'
]

master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
