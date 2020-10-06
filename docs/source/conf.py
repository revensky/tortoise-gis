import os
import sys


sys.path.insert(0, os.path.join("..", "src", "tortoise_gis"))

project = "Tortoise GIS"
copyright = "2020, Eduardo Ribeiro Rezende"  # pylint: disable=redefined-builtin
author = "Eduardo Ribeiro Rezende"
release = "0.1.2"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]

source_suffix = ".rst"
master_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
