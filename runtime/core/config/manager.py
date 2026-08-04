"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/core/config/manager.py

Purpose:
    Owns the runtime configuration.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.2.0
Release:
    Foundation Release 2
==========================================================
"""

from __future__ import annotations

from .config import RuntimeConfig


class ConfigurationManager:
    """
    Owns the application's configuration.

    Future versions will support loading and saving
    configuration from disk. For now, the manager provides
    a single shared configuration object.
    """

    def __init__(self) -> None:
        self._config = RuntimeConfig()

    @property
    def config(self) -> RuntimeConfig:
        """
        Return the active runtime configuration.
        """
        return self._config

    def reset(self) -> None:
        """
        Restore the default configuration.
        """
        self._config = RuntimeConfig()