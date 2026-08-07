"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/math.py

Purpose:
    System Math Skill

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.8
==========================================================
"""

from __future__ import annotations

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult

from .math_parser import MathParser
from .math_translator import MathTranslator


class MathSkill(Skill):

    def __init__(self) -> None:

        self._translator = MathTranslator()
        self._parser = MathParser()

    @property
    def name(self) -> str:
        return "Math"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:

        expression = self._translator.translate(
            context.request
        )

        #
        # TEMP DEBUG
        #
        print()
        print("Math Input :", context.request)
        print("Expression :", expression)
        print()

        try:

            answer = self._parser.evaluate(
                expression
            )

            if isinstance(answer, float):

                if answer.is_integer():
                    answer = int(answer)
                else:
                    answer = round(answer, 10)

            return SkillResult(
                message=f"The answer is {answer}."
            )

        except Exception as error:

            print(error)

            return SkillResult(
                message="I couldn't calculate that."
            )