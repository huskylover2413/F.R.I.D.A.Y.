"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/pulse/lifecycle.py

Purpose:
    Tracks and reports the lifecycle of services managed
    by the Pulse Runtime.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.3 - Pulse
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict

from runtime.registry import Service, ServiceState


@dataclass
class LifecycleRecord:
    """
    Stores the current lifecycle information for one service.
    """

    name: str
    state: ServiceState
    last_updated: datetime = field(default_factory=datetime.now)
    notes: str = ""

    def update(
        self,
        state: ServiceState,
        notes: str = "",
    ) -> None:
        """
        Update the lifecycle state.
        """

        self.state = state
        self.notes = notes
        self.last_updated = datetime.now()


class LifecycleManager:
    """
    Tracks the state of every registered service.
    """

    def __init__(self) -> None:
        self._records: Dict[str, LifecycleRecord] = {}

    def register(self, service: Service) -> None:
        """
        Begin tracking a service.
        """

        self._records[service.name] = LifecycleRecord(
            name=service.name,
            state=service.state,
        )

    def refresh(self, service: Service) -> None:
        """
        Refresh the current state of a service.
        """

        record = self._records.get(service.name)

        if record is None:
            self.register(service)
            return

        record.update(service.state)

    def update(
        self,
        service_name: str,
        state: ServiceState,
        notes: str = "",
    ) -> None:
        """
        Update a service manually.
        """

        record = self._records.get(service_name)

        if record is None:
            self._records[service_name] = LifecycleRecord(
                name=service_name,
                state=state,
                notes=notes,
            )
            return

        record.update(state, notes)

    def all(self) -> Dict[str, LifecycleRecord]:
        """
        Return all tracked services.
        """

        return self._records

    def healthy(self) -> bool:
        """
        Returns True when no service has failed.
        """

        return all(
            record.state != ServiceState.FAILED
            for record in self._records.values()
        )