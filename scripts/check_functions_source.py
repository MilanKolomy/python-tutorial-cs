"""Kontroluje technické části českého překladu vestavěných funkcí."""

from __future__ import annotations

import difflib
import re
import subprocess
import sys
from pathlib import Path

from check_code_blocks import extract_code_blocks_from_text


OBJECT_DIRECTIVES = {
    "attribute",
    "audit-event",
    "awaitablefunction",
    "class",
    "decorator",
    "doctest",
    "function",
    "productionlist",
    "testcode",
}
DIRECTIVE_RE = re.compile(r"^(?P<indent>\s*)\.\.\s+(?P<name>[\w-]+)::(?P<value>.*)$")
LABEL_RE = re.compile(r"(?m)^\s*\.\.\s+(_[^:]+:)\s*$")
LITERAL_RE = re.compile(r"``(.*?)``", re.DOTALL)
ROLE_RE = re.compile(r":([\w+.-]+):`([^`]*)`")
URL_RE = re.compile(r"https?://[^\s>`]+")
UPSTREAM_COMMIT = "c63aec69bd59c55314c06c23f4c22c03de76fe45"


def upstream_text(project_root: Path) -> str:
    repository = project_root / "upstream-cpython"
    command = [
        "git",
        "-c",
        f"safe.directory={repository.as_posix()}",
        "-C",
        str(repository),
        "show",
        f"{UPSTREAM_COMMIT}:Doc/library/functions.rst",
    ]
    result = subprocess.run(command, capture_output=True, check=True)
    return result.stdout.decode("utf-8")


def directive_signatures(text: str) -> list[str]:
    lines = text.splitlines()
    signatures: list[str] = []
    index = 0
    while index < len(lines):
        match = DIRECTIVE_RE.match(lines[index])
        if not match or match.group("name") not in OBJECT_DIRECTIVES:
            index += 1
            continue
        indent = len(match.group("indent"))
        block = [f'{match.group("name")}::{match.group("value")}']
        index += 1
        while index < len(lines) and lines[index].strip():
            line = lines[index]
            current_indent = len(line) - len(line.lstrip(" "))
            if current_indent <= indent:
                break
            block.append(line[indent + 1 :])
            index += 1
        signatures.append("\n".join(block))
    return signatures


def role_targets(text: str) -> list[tuple[str, str]]:
    targets: list[tuple[str, str]] = []
    for match in ROLE_RE.finditer(text):
        role, content = match.groups()
        explicit = re.search(r"<([^<>]+)>\s*$", content)
        target = explicit.group(1) if explicit else content
        targets.append((role, re.sub(r"\s+", " ", target.lstrip("~")).strip()))
    return targets


def technical_parts(text: str) -> dict[str, object]:
    return {
        "bloky kódu": [block.content for block in extract_code_blocks_from_text(text)],
        "inline kód": LITERAL_RE.findall(text),
        "signatury a technické direktivy": directive_signatures(text),
        "cíle rolí": role_targets(text),
        "štítky": LABEL_RE.findall(text),
        "URL": URL_RE.findall(text),
    }


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    translated_path = project_root / "source" / "library" / "functions.rst"
    original = technical_parts(upstream_text(project_root))
    translated = technical_parts(translated_path.read_text(encoding="utf-8"))
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
                tofile="source/library/functions.rst",
                lineterm="",
            )
        )

    if errors:
        print("\n".join(errors))
        return 1
    print("OK: technické části vestavěných funkcí odpovídají CPythonu 3.14.6.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
