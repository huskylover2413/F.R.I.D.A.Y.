"""
==========================================================
F.R.I.D.A.Y.

Apple Platform Package

Author:
    Shae Simpson & OpenAI ChatGPT
==========================================================
"""

from .permissions import ApplePermissions
from .speech import AppleSpeech

__all__ = [
    "ApplePermissions",
    "AppleSpeech",
]