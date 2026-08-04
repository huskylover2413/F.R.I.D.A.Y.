"""
==========================================================
F.R.I.D.A.Y.
Decision Demo

Purpose:
    Demonstrates the complete Speech -> Intent ->
    Decision pipeline.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.5.0
Release:
    Decision
==========================================================
"""

from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine


def demonstrate(text: str) -> None:
    """
    Demonstrate the complete reasoning pipeline.
    """

    intent_engine = IntentEngine()
    decision_engine = DecisionEngine()

    intent = intent_engine.analyze(text)

    decision = decision_engine.decide(intent)

    print("------------------------------------------")
    print(f"Input      : {text}")
    print(f"Intent     : {intent.intent.name}")
    print(f"Decision   : {decision.decision.name}")
    print()


def main() -> None:
    """
    Demonstrate FRIDAY reasoning.
    """

    print()
    print("==========================================")
    print("FRIDAY Decision Demonstration")
    print("==========================================")
    print()

    demonstrate("Hello FRIDAY")

    demonstrate("What time is it?")

    demonstrate("What is today's date?")

    demonstrate("Tell me a joke")


if __name__ == "__main__":
    main()