"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/registry/registry.py

Purpose:
    Maintains the collection of services that make up the
    FRIDAY runtime.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.3 - Pulse
==========================================================
"""

from __future__ import annotations

from typing import Dict, Iterable

from runtime.registry.service import Service


class ServiceRegistry:
    """
    Stores and manages all registered FRIDAY services.

    The registry does not start or stop services.
    It only knows which services exist.
    """

    def __init__(self) -> None:
        self._services: Dict[str, Service] = {}

    def register(self, service: Service) -> None:
        """
        Register a new service.

        Raises:
            ValueError if the service name already exists.
        """

        if service.name in self._services:
            raise ValueError(
                f"Service '{service.name}' is already registered."
            )

        self._services[service.name] = service

    def unregister(self, name: str) -> None:
        """
        Remove a service from the registry.
        """

        self._services.pop(name, None)

    def get(self, name: str) -> Service:
        """
        Return a registered service.

        Raises:
            KeyError if the service is not registered.
        """

        return self._services[name]

    def exists(self, name: str) -> bool:
        """
        Returns True if a service is registered.
        """

        return name in self._services

    def all(self) -> Iterable[Service]:
        """
        Return all registered services.
        """

        return self._services.values()

    def count(self) -> int:
        """
        Return the number of registered services.
        """

        return len(self._services)

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()