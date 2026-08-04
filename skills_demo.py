"""
==========================================================
F.R.I.D.A.Y.
Skills Demo

Purpose:
    Demonstrates the complete reasoning pipeline.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.1
==========================================================
"""

from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine
from runtime.skills import SkillRegistry
from runtime.skills.system import (
    DateSkill,
    GreetingSkill,
    TimeSkill,
)


def main() -> None:

    registry = SkillRegistry()

    registry.register(GreetingSkill())
    registry.register(TimeSkill())
    registry.register(DateSkill())

    decision_engine = DecisionEngine()
    intent_engine = IntentEngine()

    tests = [
        "Hello FRIDAY",
        "What time is it?",
        "What is today's date?",
    ]

    print()
    print("==========================================")
    print("FRIDAY Skills Demonstration")
    print("==========================================")

    for text in tests:

        intent = intent_engine.analyze(text)

        decision = decision_engine.decide(intent)

        print()
        print(f"Input: {text}")

        if decision.skill_name is None:
            print("No skill found.")
            continue

        skill = registry.get(decision.skill_name)

        result = skill.execute()

        print(f"Intent : {intent.intent.name}")
        print(f"Skill  : {decision.skill_name}")
        print(f"Reply  : {result.message}")


if __name__ == "__main__":
    main()