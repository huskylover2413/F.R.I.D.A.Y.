"""
==========================================================
F.R.I.D.A.Y.

System Skills Package

Author:
    Shae Simpson & OpenAI ChatGPT
==========================================================
"""

from .date import DateSkill
from .greeting import GreetingSkill
from .help import HelpSkill
from .identity import IdentitySkill
from .math import MathSkill
from .time import TimeSkill

__all__ = [
    "GreetingSkill",
    "TimeSkill",
    "DateSkill",
    "HelpSkill",
    "IdentitySkill",
    "MathSkill",
]