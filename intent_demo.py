"""
==========================================================
F.R.I.D.A.Y.
Intent Demo

Purpose:
    Demonstrates the Intent Engine.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.5.0
Release:
    Intent
==========================================================
"""

from runtime.intent import IntentEngine


def test(engine: IntentEngine, text: str) -> None:
    """
    Run a single intent test.
    """

    result = engine.analyze(text)

    print("------------------------------------------")
    print(f"Input      : {text}")
    print(f"Intent     : {result.intent.name}")
    print(f"Confidence : {result.confidence:.2f}")
    print()


def main() -> None:
    """
    Demonstrate the Intent Engine.
    """

    engine = IntentEngine()

    print()
    print("==========================================")
    print("FRIDAY Intent Demonstration")
    print("==========================================")
    print()

    test(engine, "Hello FRIDAY")
    test(engine, "What time is it?")
    test(engine, "What is today's date?")
    test(engine, "Tell me a joke")


if __name__ == "__main__":
    main()