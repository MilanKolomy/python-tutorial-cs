"""Porovná bloky kódu v upstreamu a v české pracovní kopii tutorialu."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DIRECTIVE_RE = re.compile(
    r"^(?P<indent>[ \t]*)\.\.\s+"
    r"(?:code-block|doctest|testcode|testoutput|testsetup)::(?:\s+.*)?$"
)


@dataclass(frozen=True)
class CodeBlock:
    line: int
    kind: str
    content: tuple[str, ...]


def indentation(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def read_indented_block(lines: list[str], start: int, parent_indent: int) -> tuple[int, tuple[str, ...]]:
    index = start
    while index < len(lines) and (not lines[index].strip() or lines[index].lstrip().startswith(":")):
        index += 1

    content_start = index
    content: list[str] = []
    content_indent = indentation(lines[content_start]) if content_start < len(lines) else parent_indent + 1
    while index < len(lines):
        line = lines[index]
        if line.strip() and indentation(line) < content_indent:
            break
        content.append(line)
        index += 1

    while content and not content[-1].strip():
        content.pop()
    if not content:
        return index, ()

    nonblank_indents = [indentation(line) for line in content if line.strip()]
    trim = min(nonblank_indents)
    normalized = tuple(line[trim:] if line.strip() else "" for line in content)
    return index, normalized


def extract_code_blocks(path: Path) -> list[CodeBlock]:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[CodeBlock] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        directive = DIRECTIVE_RE.match(line)
        if directive:
            end, content = read_indented_block(lines, index + 1, len(directive.group("indent")))
            blocks.append(CodeBlock(index + 1, "directive", content))
            index = max(end, index + 1)
            continue

        if line.rstrip().endswith("::") and not line.lstrip().startswith(".. "):
            end, content = read_indented_block(lines, index + 1, indentation(line))
            if content:
                blocks.append(CodeBlock(index + 1, "literal", content))
                index = max(end, index + 1)
                continue
        index += 1
    return blocks


def compare_file(upstream: Path, translated: Path) -> list[str]:
    original = extract_code_blocks(upstream)
    current = extract_code_blocks(translated)
    errors: list[str] = []
    if len(original) != len(current):
        errors.append(
            f"{translated.name}: počet bloků se liší "
            f"(upstream {len(original)}, source {len(current)})"
        )

    for number, (left, right) in enumerate(zip(original, current), start=1):
        if left.content == right.content:
            continue
        errors.append(
            f"{translated.name}: blok {number} se liší "
            f"(upstream ř. {left.line}, source ř. {right.line})"
        )
        errors.extend(
            difflib.unified_diff(
                left.content,
                right.content,
                fromfile=f"upstream/{upstream.name}:{left.line}",
                tofile=f"source/{translated.name}:{right.line}",
                lineterm="",
            )
        )
    return errors


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--upstream",
        type=Path,
        default=project_root / "upstream-cpython" / "Doc" / "tutorial",
    )
    parser.add_argument(
        "--source", type=Path, default=project_root / "source" / "tutorial"
    )
    args = parser.parse_args()

    errors: list[str] = []
    upstream_files = {path.name: path for path in args.upstream.glob("*.rst")}
    source_files = {path.name: path for path in args.source.glob("*.rst")}
    for missing in sorted(upstream_files.keys() - source_files.keys()):
        errors.append(f"Chybí source/tutorial/{missing}")
    for extra in sorted(source_files.keys() - upstream_files.keys()):
        errors.append(f"Soubor {extra} nemá upstreamový protějšek")
    for name in sorted(upstream_files.keys() & source_files.keys()):
        errors.extend(compare_file(upstream_files[name], source_files[name]))

    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: bloky kódu jsou shodné ve {len(upstream_files)} souborech.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
