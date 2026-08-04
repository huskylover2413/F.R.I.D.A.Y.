"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/devices/microphone/device.py

Purpose:
    Defines the microphone device interface.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class MicrophoneDevice(ABC):
    """
    Base interface for all microphone devices.
    """

    @abstractmethod
    def listen(self) -> bytes:
        """
        Capture raw audio from the microphone.

        Returns:
            Raw PCM audio bytes.
        """
        raise NotImplementedError