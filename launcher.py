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

Foundation Release:
    7
==========================================================
"""

from __future__ import annotations

from runtime.pulse import Runtime
from runtime.session import Session


def main() -> int:
    """
    Launch the FRIDAY runtime.
    """

    runtime = Runtime()

    try:
        #
        # Bring the operating environment online.
        #
        runtime.initialize()
        runtime.start()

        #
        # Begin an interactive user session.
        #
        session = Session()
        session.initialize()
        session.run()

        return 0

    except KeyboardInterrupt:

        print("\nShutdown requested.")

        return 0

    except Exception as exc:

        print("\nFRIDAY encountered a fatal startup error.")
        print(f"\nReason: {exc}")

        return 1

    finally:
        #
        # Runtime always shuts down cleanly.
        #
        runtime.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())