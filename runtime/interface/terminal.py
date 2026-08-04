"""
==========================================================
F.R.I.D.A.Y.

Terminal Interface
==========================================================
"""

from runtime.cognition import CognitionEngine


class TerminalInterface:
    """
    Keyboard interface for FRIDAY.
    """

    def __init__(
        self,
        cognition: CognitionEngine,
    ) -> None:

        self._cognition = cognition

    def run(self) -> None:

        print()
        print("══════════════════════════════════════════════")
        print("              F.R.I.D.A.Y.")
        print("══════════════════════════════════════════════")
        print()
        print("Type 'exit' to quit.")
        print()

        while True:

            text = input("> ").strip()

            if not text:
                continue

            if text.lower() in (
                "exit",
                "quit",
            ):
                print()
                print("Goodbye, Shae.")
                print()
                break

            response = self._cognition.process(
                text
            )

            print()
            print(response.message)
            print()