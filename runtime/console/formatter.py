"""
==========================================================
F.R.I.D.A.Y.
Formatter

Purpose:
    Creates consistent console output.

==========================================================
"""

from runtime.console.theme import DEFAULT_THEME


def banner(title: str) -> str:
    return (
        f"\n"
        f"{DEFAULT_THEME.title_line}\n"
        f"      {DEFAULT_THEME.app_name}\n"
        f"{DEFAULT_THEME.title_line}\n"
        f"{title}\n"
        f"{DEFAULT_THEME.title_line}\n"
    )


def line(level: str, message: str) -> str:
    return f"{level:<10}{message}"