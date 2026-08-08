"""
==========================================================
F.R.I.D.A.Y.

Memory Manager

Foundation Release 2.1
==========================================================
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from .models import Memory


class MemoryManager:

    def __init__(self) -> None:

        self._directory = (
            Path("brain")
            / "memory"
        )

        self._directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def remember(
        self,
        category: str,
        key: str,
        value: str,
    ) -> None:

        now = datetime.now()

        path = (
            self._directory
            / f"{key}.json"
        )

        created = now

        if path.exists():

            data = json.loads(
                path.read_text()
            )

            created = datetime.fromisoformat(
                data["created"]
            )

        memory = Memory(
            category=category,
            key=key,
            value=value,
            created=created,
            updated=now,
        )

        payload = asdict(memory)

        payload["created"] = memory.created.isoformat()
        payload["updated"] = memory.updated.isoformat()

        path.write_text(
            json.dumps(
                payload,
                indent=4,
            )
        )

    def recall(
        self,
        key: str,
    ) -> str | None:

        path = (
            self._directory
            / f"{key}.json"
        )

        if not path.exists():

            return None

        data = json.loads(
            path.read_text()
        )

        return data["value"]

    def search(
        self,
        text: str,
    ) -> list[Memory]:

        matches = []

        text = text.lower()

        for file in self._directory.glob("*.json"):

            data = json.loads(
                file.read_text()
            )

            haystack = (
                data["key"]
                + " "
                + data["value"]
                + " "
                + data["category"]
            ).lower()

            if text in haystack:

                matches.append(

                    Memory(
                        category=data["category"],
                        key=data["key"],
                        value=data["value"],
                        created=datetime.fromisoformat(
                            data["created"]
                        ),
                        updated=datetime.fromisoformat(
                            data["updated"]
                        ),
                    )

                )

        return matches

    def all(self) -> list[Memory]:

        memories = []

        for file in self._directory.glob("*.json"):

            data = json.loads(
                file.read_text()
            )

            memories.append(

                Memory(
                    category=data["category"],
                    key=data["key"],
                    value=data["value"],
                    created=datetime.fromisoformat(
                        data["created"]
                    ),
                    updated=datetime.fromisoformat(
                        data["updated"]
                    ),
                )

            )

        memories.sort(
            key=lambda m: m.updated,
            reverse=True,
        )

        return memories