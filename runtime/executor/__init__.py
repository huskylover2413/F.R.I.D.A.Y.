"""
==========================================================
F.R.I.D.A.Y.

Task Executor

Foundation Release 25.1
==========================================================
"""

from .executor import TaskExecutor
from .models import ExecutionResult

__all__ = [
    "TaskExecutor",
    "ExecutionResult",
]