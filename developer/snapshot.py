"""
==========================================================
F.R.I.D.A.Y.

Developer Snapshot

Foundation Release 20.2
==========================================================
"""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "build",
    "dist",
}


def iter_project_files(path: Path):

    for item in path.rglob("*"):

        if any(part in IGNORE_DIRS for part in item.parts):
            continue

        yield item


def count_files(extension: str) -> int:

    return sum(
        1
        for file in iter_project_files(PROJECT_ROOT)
        if file.is_file() and file.suffix == extension
    )


def runtime_modules():

    runtime = PROJECT_ROOT / "runtime"

    return sorted(
        folder.name
        for folder in runtime.iterdir()
        if folder.is_dir()
        and not folder.name.startswith("__")
    )


def run():

    print()

    print("══════════════════════════════════════")
    print("        FRIDAY Project Snapshot")
    print("══════════════════════════════════════")

    print()

    print("Runtime Modules")

    print("----------------")

    for module in runtime_modules():

        print(f"• {module}")

    print()

    print("Statistics")

    print("----------")

    print(f"Python Files : {count_files('.py')}")

    print(f"Markdown     : {count_files('.md')}")

    print()