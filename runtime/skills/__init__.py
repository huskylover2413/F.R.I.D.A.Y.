"""
FRIDAY Skill subsystem.
"""

from .base import Skill
from .models import SkillResult
from .registry import SkillRegistry
from .service import SkillService

__all__ = [
    "Skill",
    "SkillResult",
    "SkillRegistry",
    "SkillService",
]