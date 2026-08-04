"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    builder/project.py

Purpose:
    Provides project inspection and verification services
    for Forge. This module never prints directly—it returns
    structured results that Forge can display.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.2 - Forge
==========================================================
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from builder.blueprint import (
    FileBlueprint,
    FolderBlueprint,
    get_required_files,
    get_required_folders,
)


# ==========================================================
# Verification Models
# ==========================================================


@dataclass(frozen=True)
class CheckResult:
    """
    Represents the result of checking one file or folder.
    """

    path: Path
    exists: bool
    description: str


@dataclass(frozen=True)
class ProjectStatus:
    """
    Represents the overall health of the project.
    """

    folders: List[CheckResult]
    files: List[CheckResult]

    @property
    def healthy(self) -> bool:
        return all(item.exists for item in self.folders + self.files)


# ==========================================================
# Internal Helpers
# ==========================================================


def _check_folder(folder: FolderBlueprint) -> CheckResult:
    return CheckResult(
        path=folder.path,
        exists=folder.path.is_dir(),
        description=folder.description,
    )


def _check_file(file: FileBlueprint) -> CheckResult:
    return CheckResult(
        path=file.path,
        exists=file.path.is_file(),
        description=file.description,
    )


# ==========================================================
# Public API
# ==========================================================


def verify_project() -> ProjectStatus:
    """
    Verifies the current FRIDAY project structure against
    the Blueprint.
    """

    folder_results = [
        _check_folder(folder)
        for folder in get_required_folders()
    ]

    file_results = [
        _check_file(file)
        for file in get_required_files()
    ]

    return ProjectStatus(
        folders=folder_results,
        files=file_results,
    )