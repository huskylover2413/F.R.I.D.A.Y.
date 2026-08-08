"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    smoke_test.py

Purpose:
    Performs a basic validation of the FRIDAY platform.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.1
Release:
    Platform Freeze
==========================================================
"""

from __future__ import annotations

import sys

from launcher import main


def run_smoke_test() -> int:
    """
    Execute the FRIDAY smoke test.

    Returns:
        Exit code.
    """

    print()

    print("==========================================")
    print("FRIDAY Platform Smoke Test")
    print("==========================================")

    try:

        main()

    except Exception as exc:

        print()
        print("SMOKE TEST FAILED")
        print("------------------------------------------")
        print(exc)

        return 1

    print()
    print("------------------------------------------")
    print("SMOKE TEST PASSED")
    print("------------------------------------------")

    return 0


if __name__ == "__main__":
    sys.exit(run_smoke_test())