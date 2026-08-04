"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/paths.py

Purpose:
    Defines every important location within the FRIDAY
    project. This is the single source of truth for
    project paths.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.2 – Forge
==========================================================
"""

from pathlib import Path


# ---------------------------------------------------------
# Project Root
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Core Project Folders
# ---------------------------------------------------------

BUILDER = PROJECT_ROOT / "builder"
RUNTIME = PROJECT_ROOT / "runtime"
TOOLS = PROJECT_ROOT / "tools"

DOCS = PROJECT_ROOT / "docs"
DATA = PROJECT_ROOT / "data"
CONFIG = PROJECT_ROOT / "config"
ASSETS = PROJECT_ROOT / "assets"
TESTS = PROJECT_ROOT / "tests"

SERVICES = PROJECT_ROOT / "services"
SKILLS = PROJECT_ROOT / "skills"
INTERFACE = PROJECT_ROOT / "interface"
DEVICES = PROJECT_ROOT / "devices"


# ---------------------------------------------------------
# Root Files
# ---------------------------------------------------------

README = PROJECT_ROOT / "README.md"
LICENSE = PROJECT_ROOT / "LICENSE"
VERSION = PROJECT_ROOT / "VERSION"

PYPROJECT = PROJECT_ROOT / "pyproject.toml"
REQUIREMENTS = PROJECT_ROOT / "requirements.txt"
GITIGNORE = PROJECT_ROOT / ".gitignore"

LAUNCHER = PROJECT_ROOT / "launcher.py"