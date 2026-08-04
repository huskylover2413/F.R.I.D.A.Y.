"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/pulse/runtime.py

Purpose:
    Starts and supervises the FRIDAY runtime.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from runtime.core import CoreServices
from runtime.loader import ServiceLoader
from runtime.registry import Service, ServiceRegistry

from .state import RuntimeState


class Runtime:
    """
    Pulse is responsible for managing the lifecycle of
    every FRIDAY service.
    """

    def __init__(self) -> None:
        self.core = CoreServices.create()
        self.registry = ServiceRegistry()
        self.loader = ServiceLoader()
        self.state = RuntimeState.STOPPED

    def initialize(self) -> None:
        """
        Initialize the runtime.
        """

        self.state = RuntimeState.INITIALIZING

        self.core.console.header("Pulse Runtime")

        self.core.console.system("Initializing FRIDAY...")
        self.core.console.info("Creating service registry...")

        self.core.console.success("Core Services ready.")
        self.core.console.success("Service registry ready.")

        self.core.console.info("Loading services...")

        for service in self.loader.load():
            self.register_service(service)

        self.core.console.success(
            f"{self.registry.count()} service(s) loaded."
        )

    def register_service(self, service: Service) -> None:
        """
        Register a service with the runtime.
        """

        self.registry.register(service)

        self.core.console.info(
            f"Registered: {service.name}"
        )

    def start(self) -> None:
        """
        Start every registered service.
        """

        self.state = RuntimeState.RUNNING

        self.core.console.info("Starting services...")

        if self.registry.count() == 0:

            self.core.console.warning(
                "No services have been registered."
            )

        for service in self.registry.all():

            self.core.console.info(
                f"Starting {service.name}..."
            )

            try:

                service.start()

                if service.healthy:

                    self.core.console.success(
                        f"{service.name} running."
                    )

                else:

                    self.core.console.warning(
                        f"{service.name} started in degraded mode."
                    )

            except Exception as exc:

                self.core.console.error(
                    f"{service.name} failed to start: {exc}"
                )

        self.core.console.success(
            "Runtime startup complete."
        )

    def shutdown(self) -> None:
        """
        Stop every registered service.
        """

        self.state = RuntimeState.STOPPING

        self.core.console.info(
            "Stopping services..."
        )

        for service in reversed(
            list(self.registry.all())
        ):

            self.core.console.info(
                f"Stopping {service.name}..."
            )

            try:

                service.stop()

            except Exception as exc:

                self.core.console.error(
                    f"{service.name} failed to stop: {exc}"
                )

        self.state = RuntimeState.STOPPED

        self.core.console.success(
            "Runtime stopped."
        )