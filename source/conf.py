import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "Tutorial Pythonu"
author = "Python Software Foundation; neoficiální český překlad"
copyright = "2001–2026 Python Software Foundation; neoficiální český překlad"

version = "3.14"
release = "3.14.6"
language = "cs"

root_doc = "index"
source_suffix = ".rst"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

extensions = ["sphinx.ext.doctest", "sphinx.ext.intersphinx", "cpython_compat"]
templates_path = ["_templates"]
html_theme = "alabaster"
html_theme_options = {
    "page_width": "1080px",
    "sidebar_width": "350px",
}
html_title = "Tutorial Pythonu 3.14.6 – neoficiální český překlad"
html_static_path = ["_static"]
html_css_files = ["site.css"]
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
    "classoptions": ",oneside,openany",
    "fontpkg": r"""
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}
\newfontfamily\cjkfont{Yu Gothic}
""",
    "sphinxsetup": "verbatimwrapslines=true,verbatimforcewraps=true",
    "preamble": r"""
\usepackage{newunicodechar}
\newunicodechar{景}{{\cjkfont 景}}
\newunicodechar{太}{{\cjkfont 太}}
\newunicodechar{郎}{{\cjkfont 郎}}
\renewcommand{\literalblockcontinuesname}{pokračování na další straně}
\setlength{\emergencystretch}{3em}
""",
    "maketitle": r"""
\makeatletter
\hypersetup{
  pdftitle={\@title},
  pdfauthor={Python Software Foundation; Milan Kolomý},
  pdfsubject={Neoficiální český překlad tutorialu Pythonu 3.14.6},
  pageanchor=false
}
\begin{titlepage}
  \centering
  \vspace*{0.14\textheight}
  {\Huge\bfseries \@title\par}
  \vspace{1.4cm}
  {\Large Neoficiální český překlad\par}
  \vfill
  {\large © 2001--2026 Python Software Foundation\par}
  \vspace{0.45cm}
  {\large Vytvořil Milan Kolomý za pomocí ChatGPT Codex\par}
  \vspace{1.2cm}
  {\small Vygenerováno pomocí Sphinx 8.2.3 a LuaLaTeX.\par}
  \vspace{0.25cm}
  {\small Zdrojová verze:\par}
  {\small\url{https://github.com/MilanKolomy/python-tutorial-cs}\par}
\end{titlepage}
\hypersetup{pageanchor=true}
\makeatother
\clearpage
""",
}

latex_show_urls = "footnote"
