"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    launcher.py

Purpose:
    Official entry point for FRIDAY.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.4 - Foundation Release 2
==========================================================
"""

from __future__ import annotations

import sys

from runtime.pulse import Runtime


def main() -> int:
    """
    Launch the FRIDAY runtime.

    Returns:
        int: Process exit code.
    """
    try:
        runtime = Runtime()
        runtime.initialize()
        runtime.start()
        return 0

    except KeyboardInterrupt:
        print("\nShutdown requested by user.")
        return 0

    except Exception as exc:
        print("\nFRIDAY was unable to start.")
        print(f"Reason: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())