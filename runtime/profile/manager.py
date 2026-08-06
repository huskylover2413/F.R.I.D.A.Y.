"""
==========================================================
F.R.I.D.A.Y.
Profile Manager
==========================================================
"""

from __future__ import annotations

import json
from pathlib import Path

from .models import UserProfile


class ProfileManager:
    """
    Loads the active FRIDAY profile.
    """

    def __init__(
        self,
        path: str = "config/profile.json",
    ) -> None:

        self._path = Path(path)

    def load(self) -> UserProfile:

        data = json.loads(
            self._path.read_text(
                encoding="utf-8"
            )
        )

        return UserProfile(**data)