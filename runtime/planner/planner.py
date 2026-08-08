"""
==========================================================
F.R.I.D.A.Y.

Planner

Foundation Release 24.1
==========================================================
"""

from __future__ import annotations

from .models import Plan


class Planner:
    """
    Builds an execution plan.
    """

    def plan(
        self,
        request: str,
    ) -> Plan:

        request = request.lower()

        plan = Plan()

        #
        # Vision
        #

        if any(

            phrase in request

            for phrase in (

                "what am i looking at",

                "what's on my screen",

                "describe my screen",

                "look at my screen",

                "read my screen",

            )

        ):

            plan.add(
                "Vision"
            )

            return plan

        return plan