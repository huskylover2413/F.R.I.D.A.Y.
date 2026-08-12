"""
==========================================================
F.R.I.D.A.Y.

Date Skill

Foundation Release 49.0
==========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult


class DateSkill(Skill):
    """
    Reports date and calendar information.
    """

    @property
    def name(self) -> str:
        return "Date"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:

        now = datetime.now()

        request = ""

        if hasattr(context, "request"):
            request = str(
                context.request
            ).lower().strip()

        #
        # --------------------------------------------------
        # Tomorrow
        # --------------------------------------------------
        #

        if "tomorrow" in request:

            tomorrow = (
                now + timedelta(days=1)
            )

            return SkillResult(
                message=(
                    f"Tomorrow is "
                    f"{tomorrow.strftime('%A, %B %d, %Y')}."
                )
            )

        #
        # --------------------------------------------------
        # Yesterday
        # --------------------------------------------------
        #

        if "yesterday" in request:

            yesterday = (
                now - timedelta(days=1)
            )

            return SkillResult(
                message=(
                    f"Yesterday was "
                    f"{yesterday.strftime('%A, %B %d, %Y')}."
                )
            )

        #
        # --------------------------------------------------
        # Named day of the week
        # --------------------------------------------------
        #

        weekdays = {
            "monday": "Monday",
            "tuesday": "Tuesday",
            "wednesday": "Wednesday",
            "thursday": "Thursday",
            "friday": "Friday",
            "saturday": "Saturday",
            "sunday": "Sunday",
        }

        for day_name, display_name in weekdays.items():

            if day_name in request:

                return SkillResult(
                    message=(
                        f"{display_name} is a day "
                        f"of the week."
                    )
                )

        #
        # --------------------------------------------------
        # Day of week
        # --------------------------------------------------
        #

        if (
            "what day" in request
            or "day is it" in request
            or "day of the week" in request
            or request == "day"
        ):

            return SkillResult(
                message=(
                    f"Today is "
                    f"{now.strftime('%A')}."
                )
            )

        #
        # --------------------------------------------------
        # Month
        # --------------------------------------------------
        #

        if "month" in request:

            return SkillResult(
                message=(
                    f"It is "
                    f"{now.strftime('%B')}."
                )
            )

        #
        # --------------------------------------------------
        # Year
        # --------------------------------------------------
        #

        if "year" in request:

            return SkillResult(
                message=(
                    f"It is "
                    f"{now.strftime('%Y')}."
                )
            )

        #
        # --------------------------------------------------
        # Today
        # --------------------------------------------------
        #

        if (
            "today" in request
            or "current date" in request
            or "what date is it" in request
            or "what is the date" in request
            or "what's the date" in request
        ):

            return SkillResult(
                message=(
                    f"Today is "
                    f"{now.strftime('%A, %B %d, %Y')}."
                )
            )

        #
        # --------------------------------------------------
        # Default
        # --------------------------------------------------
        #

        return SkillResult(
            message=(
                f"Today is "
                f"{now.strftime('%A, %B %d, %Y')}."
            )
        )