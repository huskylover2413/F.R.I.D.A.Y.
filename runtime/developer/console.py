"""
==========================================================
F.R.I.D.A.Y.

Developer Console

Foundation Release 2.3
==========================================================
"""

from __future__ import annotations

import os


class DeveloperConsole:

    def run(self) -> None:

        while True:

            os.system("clear")

            print()

            print("══════════════════════════════════════")
            print("      F.R.I.D.A.Y. Developer")
            print("══════════════════════════════════════")
            print()

            print("1. Launch FRIDAY")
            print("2. Test Vision")
            print("3. Test Memory")
            print("4. Test Planner")
            print("5. Test AI")
            print("6. System Diagnostics")
            print("0. Exit")

            print()

            choice = input("> ")

            if choice == "0":
                break

            print()
            print("Coming soon...")
            input("\nPress ENTER...")