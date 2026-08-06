"""
FRIDAY Input subsystem.
"""

from .keyboard import KeyboardInput
from .microphone import MicrophoneInput
from .service import InputService
from .source import InputSource

__all__ = [
    "InputSource",
    "KeyboardInput",
    "MicrophoneInput",
    "InputService",
]