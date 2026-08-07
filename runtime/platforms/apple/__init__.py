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
<<<<<<< HEAD

__all__ = [
    "ApplePermissions",
=======
from .speech.provider import AppleSpeechProvider

__all__ = [
    "ApplePermissions",
    "AppleSpeechProvider",
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
]