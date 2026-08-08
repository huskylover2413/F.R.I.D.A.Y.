"""
==========================================================
F.R.I.D.A.Y.
Cognition Demo

Purpose:
    Demonstrates the complete FRIDAY reasoning pipeline.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.7.0
==========================================================
"""

from runtime.cognition import CognitionEngine


def main() -> None:

    engine = CognitionEngine()

    tests = [
        "Hello FRIDAY",
        "What time is it?",
        "What is today's date?",
        "Tell me a joke",
    ]

    print()
    print("==========================================")
    print("FRIDAY Cognition Demonstration")
    print("==========================================")

    for text in tests:

        response = engine.process(text)

        print()
        print(f"You     : {text}")
        print(f"FRIDAY  : {response.message}")


if __name__ == "__main__":
    main()