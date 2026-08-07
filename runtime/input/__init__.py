"""
==========================================================
F.R.I.D.A.Y.
Input subsystem.
==========================================================
"""

from .keyboard import KeyboardInput
from .microphone import MicrophoneInput
from .source import InputSource
from .service import InputService

__all__ = [
    "InputSource",
    "KeyboardInput",
    "MicrophoneInput",
    "InputService",
]