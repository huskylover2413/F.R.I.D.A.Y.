"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

Connector Manager

Foundation Release 20.1
==========================================================
"""

from __future__ import annotations

from .base import Connector


class ConnectorManager:

    def __init__(self) -> None:

        self._connectors: dict[str, Connector] = {}

    def register(
        self,
        connector: Connector,
    ) -> None:

        self._connectors[
            connector.name.lower()
        ] = connector

    def get(
        self,
        name: str,
    ) -> Connector | None:

        return self._connectors.get(
            name.lower()
        )

    def available(self) -> list[Connector]:

        return [

            connector

            for connector in self._connectors.values()

            if connector.available()

        ]

    def all(self) -> list[Connector]:

        return list(
            self._connectors.values()
        )