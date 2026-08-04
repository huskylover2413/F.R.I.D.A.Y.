"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/loader/loader.py

Purpose:
    Creates and registers runtime services.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.1
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from runtime.registry import ServiceRegistry

from .exceptions import InvalidServiceError
from .manifest import ServiceManifest


class ServiceLoader:
    """
    Creates services defined by the Service Manifest and
    registers them with the Service Registry.
    """

    def __init__(
        self,
        registry: ServiceRegistry,
        manifest: ServiceManifest | None = None,
    ) -> None:
        self._registry = registry
        self._manifest = manifest or ServiceManifest()

    def load(self) -> int:
        """
        Instantiate and register every configured service.

        Returns:
            Number of services loaded.
        """

        count = 0

        for service_type in self._manifest.services:

            service = service_type()

            if not hasattr(service, "start"):

                raise InvalidServiceError(
                    f"{service_type.__name__} "
                    "is not a valid Runtime Service."
                )

            self._registry.register(service)

            count += 1

        return count