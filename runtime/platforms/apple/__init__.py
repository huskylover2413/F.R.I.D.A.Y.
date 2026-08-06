"""
==========================================================
F.R.I.D.A.Y.

Apple Platform Package

Purpose:
    Public Apple platform exports.

Author:
    Shae Simpson & OpenAI ChatGPT
==========================================================
"""

from .permissions import ApplePermissions
from .speech.provider import AppleSpeechProvider

__all__ = [
    "ApplePermissions",
    "AppleSpeechProvider",
]