"""
==========================================================

F.R.I.D.A.Y.

Filesystem Project Provider

Version 1.2

==========================================================
"""

from __future__ import annotations

from pathlib import Path


class FilesystemProjectProvider:
    """
    Reads information directly
    from the FRIDAY project.
    """

    def python_files(self) -> list[Path]:

        return sorted(

            Path(".")

            .rglob("*.py")

        )

    def markdown_files(self) -> list[Path]:

        return sorted(

            Path(".")

            .rglob("*.md")

        )