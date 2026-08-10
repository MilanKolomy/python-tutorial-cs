"""Opakovatelné sestavení českého tutorialu Pythonu do PDF."""

from __future__ import annotations

import argparse
import importlib.metadata
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "source"
TUTORIAL_DIR = SOURCE_DIR / "tutorial"
WORK_DIR = PROJECT_ROOT / "work" / "pdf"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "pdf"
SPHINX_VERSION = "8.2.3"
RELEASE = "3.14.6"


class BuildError(RuntimeError):
    """Chyba, kterou lze srozumitelně předat uživateli."""


@dataclass(frozen=True)
class Chapter:
    number: int
    name: str
    title: str

    @property
    def slug(self) -> str:
        normalized = unicodedata.normalize("NFKD", self.title)
        ascii_title = normalized.encode("ascii", "ignore").decode("ascii")
        slug = re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
        return slug[:80].rstrip("-") or self.name


def _is_adornment(line: str) -> bool:
    stripped = line.strip()
    return len(stripped) >= 3 and len(set(stripped)) == 1 and stripped[0] in "=-~`^\"'+#*"


def read_title(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    for index in range(len(lines) - 1):
        if lines[index].strip() and not _is_adornment(lines[index]):
            if _is_adornment(lines[index + 1]):
                return lines[index].strip()
    raise BuildError(f"V souboru {path} se nepodařilo najít nadpis kapitoly.")


def load_chapters() -> list[Chapter]:
    index_path = TUTORIAL_DIR / "index.rst"
    lines = index_path.read_text(encoding="utf-8").splitlines()
    entries: list[str] = []
    in_numbered_toctree = False
    collecting = False

    for line in lines:
        if line.strip() == ".. toctree::":
            in_numbered_toctree = False
            collecting = True
            continue
        if not collecting:
            continue
        if line.strip() == ":numbered:":
            in_numbered_toctree = True
            continue
        if not line.strip() or line.lstrip().startswith(":"):
            continue
        if line == line.lstrip():
            if in_numbered_toctree and entries:
                break
            collecting = False
            continue
        if in_numbered_toctree:
            target = line.strip()
            match = re.search(r"<([^>]+)>$", target)
            if match:
                target = match.group(1)
            entries.append(Path(target).stem)

    if not entries:
        raise BuildError(f"V {index_path} nebyl nalezen číslovaný seznam kapitol.")

    chapters: list[Chapter] = []
    for number, name in enumerate(entries, start=1):
        path = TUTORIAL_DIR / f"{name}.rst"
        if not path.is_file():
            raise BuildError(f"Chybí zdroj kapitoly: {path}")
        chapters.append(Chapter(number, name, read_title(path)))
    return chapters


def remove_document_title(text: str) -> str:
    lines = text.splitlines()
    title_index = None
    for index in range(len(lines) - 1):
        if lines[index].strip() and not _is_adornment(lines[index]):
            if _is_adornment(lines[index + 1]):
                title_index = index
                break
    if title_index is None:
        return text
    start = title_index - 1 if title_index > 0 and _is_adornment(lines[title_index - 1]) else title_index
    del lines[start : title_index + 2]
    return "\n".join(lines)


def remove_toctrees(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    index = 0
    while index < len(lines):
        if lines[index].strip() != ".. toctree::":
            result.append(lines[index])
            index += 1
            continue
        index += 1
        while index < len(lines) and (not lines[index].strip() or lines[index] != lines[index].lstrip()):
            index += 1
    return "\n".join(result).strip()


def split_terminology_table(path: Path, rows_per_table: int = 5) -> None:
    """V pracovní kopii rozdělí dlouhou list-table na zalomitelné části."""
    lines = path.read_text(encoding="utf-8").splitlines()
    directive = next(
        (index for index, line in enumerate(lines) if line.strip() == ".. list-table::"),
        None,
    )
    if directive is None:
        raise BuildError(f"V {path} nebyla nalezena očekávaná tabulka.")

    row_starts = [
        index for index in range(directive + 1, len(lines)) if lines[index].startswith("   * - ")
    ]
    if len(row_starts) <= rows_per_table + 1:
        return

    row_starts.append(len(lines))
    rows = [lines[start:end] for start, end in zip(row_starts, row_starts[1:])]
    header, data_rows = rows[0], rows[1:]
    table_options = lines[directive + 1 : row_starts[0]]
    generated = lines[:directive]

    offsets = list(range(0, len(data_rows), rows_per_table))
    page_starts = {2, 6, 9, 12}
    for chunk_index, offset in enumerate(offsets):
        starts_new_page = chunk_index in page_starts
        if starts_new_page:
            generated.extend(
                [
                    "",
                    ".. raw:: latex",
                    "",
                    "   \\clearpage\\null\\par",
                    "",
                    ".. rubric:: Terminologický slovník (pokračování)",
                    "",
                ]
            )
        elif chunk_index:
            generated.append("")
        generated.append(".. list-table::")
        generated.extend(table_options)
        generated.extend(header)
        for row in data_rows[offset : offset + rows_per_table]:
            generated.extend(row)

    path.write_text("\n".join(generated).rstrip() + "\n", encoding="utf-8")


def reset_work_dir() -> None:
    expected = (PROJECT_ROOT / "work" / "pdf").resolve()
    actual = WORK_DIR.resolve()
    if actual != expected or actual.parent != (PROJECT_ROOT / "work").resolve():
        raise BuildError(f"Odmítnuto nebezpečné čištění pracovního adresáře: {actual}")
    if actual.exists():
        shutil.rmtree(actual)
    actual.mkdir(parents=True)


def find_tool(name: str, sibling_of: Path | None = None) -> Path | None:
    executable = shutil.which(name)
    if executable:
        return Path(executable)

    suffixes = (".exe", ".bat", ".cmd") if os.name == "nt" else ("",)
    candidates: list[Path] = []
    if sibling_of:
        candidates.extend(sibling_of.parent / f"{name}{suffix}" for suffix in suffixes)

    if os.name == "nt":
        env = os.environ
        roots = [
            Path(env.get("LOCALAPPDATA", "")) / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64",
            Path(env.get("APPDATA", "")) / "TinyTeX" / "bin" / "windows",
            Path(env.get("ProgramFiles", "C:/Program Files")) / "MiKTeX" / "miktex" / "bin" / "x64",
        ]
        for root in roots:
            candidates.extend(root / f"{name}{suffix}" for suffix in suffixes)
        for texlive_root in (Path("C:/texlive"), Path(env.get("USERPROFILE", "")) / "texlive"):
            if texlive_root.is_dir():
                for bin_dir in sorted(texlive_root.glob("*/bin/windows"), reverse=True):
                    candidates.extend(bin_dir / f"{name}{suffix}" for suffix in suffixes)

    return next((path for path in candidates if path.is_file()), None)


def check_sphinx() -> None:
    try:
        installed = importlib.metadata.version("Sphinx")
    except importlib.metadata.PackageNotFoundError as exc:
        raise BuildError(
            "Chybí Sphinx. Spusťte skript Pythonem z .venv po instalaci requirements.txt."
        ) from exc
    if installed != SPHINX_VERSION:
        raise BuildError(
            f"Je vyžadován Sphinx {SPHINX_VERSION}, nalezena byla verze {installed}. "
            "Nainstalujte závislosti z requirements.txt."
        )


def check_tex_tools() -> tuple[Path, Path]:
    lualatex = find_tool("lualatex")
    makeindex = find_tool("makeindex", sibling_of=lualatex)
    missing = [name for name, value in (("lualatex", lualatex), ("makeindex", makeindex)) if value is None]
    if missing:
        raise BuildError(
            "Chybí nástroje pro vytvoření PDF: "
            + ", ".join(missing)
            + ". Nainstalujte pro Windows MiKTeX nebo TeX Live s LuaLaTeXem, "
            "potom otevřete nový terminál nebo přidejte jejich adresář bin do PATH."
        )
    return lualatex, makeindex


def choose_chapters(requested: list[str], chapters: list[Chapter]) -> list[Chapter]:
    by_name = {chapter.name: chapter for chapter in chapters}
    unknown = sorted(set(requested) - set(by_name))
    if unknown:
        raise BuildError(
            "Neznámá kapitola: "
            + ", ".join(unknown)
            + ". Dostupné názvy vypíšete pomocí --list."
        )
    selected_names = set(requested)
    return [chapter for chapter in chapters if chapter.name in selected_names]


def output_name(selected: list[Chapter] | None) -> str:
    if selected is None:
        return f"python-tutorial-cs-{RELEASE}.pdf"
    if len(selected) == 1:
        chapter = selected[0]
        return f"{chapter.number:02d}-{chapter.slug}.pdf"
    numbers = "-".join(f"{chapter.number:02d}" for chapter in selected)
    return f"python-tutorial-cs-kapitoly-{numbers}.pdf"


def document_title(selected: list[Chapter] | None) -> str:
    if selected is None:
        return f"Tutorial Pythonu {RELEASE}"
    if len(selected) == 1:
        chapter = selected[0]
        return f"Tutorial Pythonu {RELEASE} - {chapter.number}. {chapter.title}"
    numbers = ", ".join(str(chapter.number) for chapter in selected)
    return f"Tutorial Pythonu {RELEASE} - vybrané kapitoly {numbers}"


def prepare_source(selected: list[Chapter] | None, all_chapters: list[Chapter]) -> tuple[Path, str]:
    source_copy = WORK_DIR / "source"
    shutil.copytree(
        SOURCE_DIR,
        source_copy,
        ignore=shutil.ignore_patterns("_build", "__pycache__", "*.pyc"),
    )
    split_terminology_table(source_copy / "terminology.rst")

    root_body = remove_toctrees(remove_document_title((SOURCE_DIR / "index.rst").read_text(encoding="utf-8")))
    tutorial_body = remove_toctrees(
        remove_document_title((TUTORIAL_DIR / "index.rst").read_text(encoding="utf-8"))
    )

    lines = [
        f"Tutorial Pythonu {RELEASE}",
        "=" * len(f"Tutorial Pythonu {RELEASE}"),
        "",
    ]
    if selected is None:
        lines.extend(
            [
                ".. raw:: latex",
                "",
                "   \\markboth{Předmluva}{Předmluva}",
                "",
                root_body,
                "",
                ".. rubric:: Předmluva",
                "",
                tutorial_body,
                "",
            ]
        )
        included = all_chapters
    else:
        if len(selected) == 1:
            chapter = selected[0]
            lines.extend(
                [
                    ".. raw:: latex",
                    "",
                    f"   \\setcounter{{chapter}}{{{chapter.number - 1}}}",
                    "",
                ]
            )
        included = selected

    lines.extend([".. toctree::", "   :maxdepth: 4", "   :numbered:", ""])
    lines.extend(f"   tutorial/{chapter.name}" for chapter in included)

    if selected is None:
        lines.extend(["", ".. toctree::", "   :maxdepth: 2", "   :caption: Dodatky", "", "   terminology"])

    root_name = "pdf-index"
    (source_copy / f"{root_name}.rst").write_text("\n".join(lines) + "\n", encoding="utf-8")

    title = document_title(selected)
    author = "Python Software Foundation; neoficiální český překlad"
    table_of_contents = "" if selected is not None and len(selected) == 1 else r"\sphinxtableofcontents"
    override = f'''\n\n# Automaticky vytvořeno scripts/build_pdf.py pouze v work/pdf.\nroot_doc = {root_name!r}\nlatex_documents = [\n    ({root_name!r}, "python-tutorial-cs.tex", {title!r}, {author!r}, "manual"),\n]\nlatex_elements = dict(latex_elements)\nlatex_elements["tableofcontents"] = {table_of_contents!r}\n'''
    override += 'exclude_patterns = list(exclude_patterns) + ["index.rst", "tutorial/index.rst"]\n'
    override += 'suppress_warnings = list(globals().get("suppress_warnings", [])) + ["toc.not_included"]\n'
    with (source_copy / "conf.py").open("a", encoding="utf-8", newline="\n") as config:
        config.write(override)
    return source_copy, root_name


def run(
    command: list[str],
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> None:
    print("Spouštím:", subprocess.list2cmdline(command), flush=True)
    result = subprocess.run(command, cwd=cwd, env=env, check=False)
    if result.returncode:
        raise BuildError(f"Příkaz skončil s návratovým kódem {result.returncode}.")


def build(selected: list[Chapter] | None, chapters: list[Chapter]) -> Path:
    check_sphinx()
    lualatex, makeindex = check_tex_tools()
    reset_work_dir()
    source_copy, _ = prepare_source(selected, chapters)
    latex_dir = WORK_DIR / "latex"

    run(
        [
            sys.executable,
            "-m",
            "sphinx",
            "-E",
            "-a",
            "-W",
            "--keep-going",
            "-b",
            "latex",
            str(source_copy),
            str(latex_dir),
        ]
    )

    tex_env = os.environ.copy()
    tex_env["PATH"] = str(lualatex.parent) + os.pathsep + tex_env.get("PATH", "")
    lualatex_command = [
        str(lualatex),
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "python-tutorial-cs.tex",
    ]
    try:
        for _ in range(3):
            run(lualatex_command, cwd=latex_dir, env=tex_env)
        index_file = latex_dir / "python-tutorial-cs.idx"
        if index_file.is_file():
            run(
                [str(makeindex), "-s", "python.ist", index_file.name],
                cwd=latex_dir,
                env=tex_env,
            )
        for _ in range(2):
            run(lualatex_command, cwd=latex_dir, env=tex_env)
    except BuildError as exc:
        raise BuildError(
            f"LuaLaTeX sestavení selhalo. Podrobnosti jsou v "
            f"{latex_dir / 'python-tutorial-cs.log'}. {exc}"
        ) from exc

    generated = latex_dir / "python-tutorial-cs.pdf"
    if not generated.is_file():
        raise BuildError(f"Sestavení skončilo bez očekávaného souboru {generated}.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / output_name(selected)
    staged = WORK_DIR / destination.name
    shutil.copy2(generated, staged)
    os.replace(staged, destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Vytvoří PDF českého tutorialu Pythonu ze zdrojů v source/.",
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--list", action="store_true", help="vypíše dostupné kapitoly")
    selection.add_argument("--all", action="store_true", help="sestaví celý tutorial")
    selection.add_argument(
        "--chapter",
        action="append",
        metavar="NÁZEV",
        help="sestaví vybranou kapitolu; volbu lze opakovat",
    )
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        chapters = load_chapters()
        if args.list:
            for chapter in chapters:
                print(f"{chapter.number:02d}  {chapter.name:<16} {chapter.title}")
            return 0

        selected = None if args.all else choose_chapters(args.chapter, chapters)
        destination = build(selected, chapters)
        print(f"Hotovo: {destination}")
        return 0
    except BuildError as exc:
        print(f"CHYBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
