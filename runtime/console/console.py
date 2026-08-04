"""
==========================================================
F.R.I.D.A.Y.
Console

Purpose:
    Centralized console output.

==========================================================
"""

from runtime.console.formatter import banner, line


class Console:

    def header(self, title: str) -> None:
        print(banner(title))

    def info(self, message: str) -> None:
        print(line("INFO", message))

    def success(self, message: str) -> None:
        print(line("SUCCESS", message))

    def warning(self, message: str) -> None:
        print(line("WARNING", message))

    def error(self, message: str) -> None:
        print(line("ERROR", message))

    def system(self, message: str) -> None:
        print(line("SYSTEM", message))


console = Console()