"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/devices/microphone/mock_microphone.py

Purpose:
    Mock microphone used during development.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from __future__ import annotations

from .device import MicrophoneDevice


class MockMicrophone(MicrophoneDevice):
    """
    Development microphone.

    Returns empty audio data.
    """

    def listen(self) -> bytes:
        return b""