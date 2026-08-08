"""
==========================================================
F.R.I.D.A.Y.

Project Models

Foundation Release 3.3
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ProjectTask:

    title: str

    completed: bool = False


@dataclass(slots=True)
class ProjectStatus:

    name: str

    version: str

    tasks: list[ProjectTask]