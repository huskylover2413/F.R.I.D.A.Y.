"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    builder/blueprint.py

Purpose:
    Defines the official project blueprint used by Forge.
    This file is the single source of truth for the FRIDAY
    project structure.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.2 - Forge
==========================================================
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List


# ==========================================================
# Blueprint Models
# ==========================================================

@dataclass(frozen=True)
class FolderBlueprint:
    """
    Describes a required project folder.
    """

    path: Path
    description: str
    required: bool = True


@dataclass(frozen=True)
class FileBlueprint:
    """
    Describes a required project file.
    """

    path: Path
    description: str
    required: bool = True


# ==========================================================
# Project Blueprint
# ==========================================================

PROJECT_NAME = "F.R.I.D.A.Y."

PROJECT_FOLDERS: List[FolderBlueprint] = [

    FolderBlueprint(
        path=Path("builder"),
        description="Engineering platform for creating and maintaining FRIDAY."
    ),

    FolderBlueprint(
        path=Path("runtime"),
        description="Starts, supervises, and manages the FRIDAY runtime."
    ),

    FolderBlueprint(
        path=Path("tools"),
        description="Development support tools."
    ),

    FolderBlueprint(
        path=Path("docs"),
        description="Architecture, design, and engineering documentation."
    ),

]

PROJECT_FILES: List[FileBlueprint] = [

    FileBlueprint(
        path=Path("README.md"),
        description="Project overview and philosophy."
    ),

    FileBlueprint(
        path=Path("LICENSE"),
        description="Project license."
    ),

    FileBlueprint(
        path=Path("CHANGELOG.md"),
        description="Project history."
    ),

    FileBlueprint(
        path=Path("VERSION"),
        description="Current FRIDAY version."
    ),

    FileBlueprint(
        path=Path(".gitignore"),
        description="Git ignore rules."
    ),

    FileBlueprint(
        path=Path("requirements.txt"),
        description="Python dependencies."
    ),

    FileBlueprint(
        path=Path("pyproject.toml"),
        description="Python project configuration."
    ),

    FileBlueprint(
        path=Path("launcher.py"),
        description="Official FRIDAY entry point."
    ),

]


# ==========================================================
# Blueprint API
# ==========================================================

def get_required_folders() -> List[FolderBlueprint]:
    """
    Returns all required project folders.
    """
    return PROJECT_FOLDERS.copy()


def get_required_files() -> List[FileBlueprint]:
    """
    Returns all required project files.
    """
    return PROJECT_FILES.copy()