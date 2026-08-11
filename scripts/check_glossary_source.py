"""Kontroluje technické části českého překladu slovníku pojmů."""

from __future__ import annotations

import difflib
import re
import subprocess
import sys
from pathlib import Path

from check_functions_source import UPSTREAM_COMMIT, technical_parts


TERM_RE = re.compile(r"(?m)^ {3}(?!\.\.)(\S.*)\n {6}\S")
INDEX_RE = re.compile(
    r"(?m)^(?P<indent>\s*)\.\. index::(?P<value>.*)"
    r"(?P<body>(?:\n(?P=indent) {3,}[^\n]*)*)"
)


def upstream_text(project_root: Path) -> str:
    repository = project_root / "upstream-cpython"
    command = [
        "git",
        "-c",
        f"safe.directory={repository.as_posix()}",
        "-C",
        str(repository),
        "show",
        f"{UPSTREAM_COMMIT}:Doc/glossary.rst",
    ]
    result = subprocess.run(command, capture_output=True, check=True)
    return result.stdout.decode("utf-8")


def glossary_technical_parts(text: str) -> dict[str, object]:
    parts = technical_parts(text)
    # Role dfn marks translated natural-language definitions. Unlike reference
    # roles, it does not support a hidden explicit target in ``<...>``.
    parts["cíle rolí"] = [item for item in parts["cíle rolí"] if item[0] != "dfn"]
    parts["hesla slovníku"] = TERM_RE.findall(text)
    parts["indexové direktivy"] = [match.group(0) for match in INDEX_RE.finditer(text)]
    return parts


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    translated_path = project_root / "source" / "glossary.rst"
    original = glossary_technical_parts(upstream_text(project_root))
    translated = glossary_technical_parts(translated_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    for name, expected in original.items():
        actual = translated[name]
        if expected == actual:
            continue
        errors.append(f"Technická část „{name}“ se liší od CPythonu 3.14.6.")
        left = [repr(item) for item in expected]
        right = [repr(item) for item in actual]
        errors.extend(
            difflib.unified_diff(
                left,
                right,
                fromfile="CPython 3.14.6",
                tofile="source/glossary.rst",
                lineterm="",
            )
        )

    if errors:
        print("\n".join(errors))
        return 1
    print("OK: technické části slovníku odpovídají CPythonu 3.14.6.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
