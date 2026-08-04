"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/registry/service.py

Purpose:
    Defines the base interface that every FRIDAY service
    must implement.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.3 - Pulse
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum, auto


class ServiceState(Enum):
    """
    Represents the lifecycle state of a FRIDAY service.
    """

    STOPPED = auto()
    STARTING = auto()
    RUNNING = auto()
    DEGRADED = auto()
    STOPPING = auto()
    FAILED = auto()


class Service(ABC):
    """
    Base class for every FRIDAY service.

    All services must inherit from this class so Runtime
    can manage them consistently.
    """

    def __init__(self, name: str):
        self._name = name
        self._state = ServiceState.STOPPED

    @property
    def name(self) -> str:
        """Human-readable service name."""
        return self._name

    @property
    def state(self) -> ServiceState:
        """Current lifecycle state."""
        return self._state

    @property
    def healthy(self) -> bool:
        """
        Returns True when the service is operating normally.
        """
        return self._state in (
            ServiceState.RUNNING,
            ServiceState.DEGRADED,
        )

    @abstractmethod
    def start(self) -> None:
        """
        Start the service.
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the service.
        """
        raise NotImplementedError

    @abstractmethod
    def health_report(self) -> str:
        """
        Return a human-readable health description.
        """
        raise NotImplementedError