# Documenting Blender Python code with Sphinx
# https://stackoverflow.com/questions/49434810/documenting-blender-python-code-with-sphinx

import sys

from sphinx.cmd import build

first_sphinx_arg = sys.argv.index('-M')
build.make_main(sys.argv[first_sphinx_arg:])
