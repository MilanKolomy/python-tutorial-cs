project = "Tutorial Pythonu"
author = "Python Software Foundation; neoficiální český překlad"
copyright = "2001–2026 Python Software Foundation; neoficiální český překlad"

version = "3.14"
release = "3.14.6"
language = "cs"

root_doc = "index"
source_suffix = ".rst"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

extensions = ["sphinx.ext.doctest", "sphinx.ext.intersphinx"]
templates_path = ["_templates"]
html_theme = "alabaster"
html_theme_options = {
    "page_width": "1080px",
    "sidebar_width": "350px",
}
html_title = "Tutorial Pythonu 3.14.6 – neoficiální český překlad"
html_static_path = ["_static"]
html_js_files = ["reader-controls.js"]
html_show_sourcelink = True

# Odkazy do ostatních částí oficiální dokumentace Pythonu zůstávají zachované.
# V tomto samostatném projektu nemusí mít lokální cíl.
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/release/3.14.6/",
        "_intersphinx/python-3.14.6.inv",
    ),
}

nitpicky = False

rst_epilog = """
.. |python_x_dot_y_literal| replace:: ``python3.14``
.. |usr_local_bin_python_x_dot_y_literal| replace:: ``/usr/local/bin/python3.14``
"""

latex_engine = "lualatex"
latex_documents = [
    (
        "index",
        "python-tutorial-cs.tex",
        "Tutorial Pythonu 3.14.6",
        "Python Software Foundation; neoficiální český překlad",
        "manual",
    )
]
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    "fontpkg": r"""
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}
""",
}
