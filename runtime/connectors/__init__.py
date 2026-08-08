"""
FRIDAY Connector Framework.
"""

from .base import Connector
from .manager import ConnectorManager

__all__ = [
    "Connector",
    "ConnectorManager",
]