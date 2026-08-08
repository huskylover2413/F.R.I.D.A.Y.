"""
==========================================================
F.R.I.D.A.Y.

AI Planner

Version 2.0.1
==========================================================
"""

from __future__ import annotations

import json

import requests


class AIPlannerProvider:

    def __init__(self):

        self._model = "llama3.2:3b"

    def plan(
        self,
        request: str,
    ) -> list[str]:

        prompt = f"""
You are FRIDAY's planner.

Choose one or more tools.

Allowed tool names ONLY:

Conversation
Vision
Math
Memory

Respond ONLY with a JSON array.

Examples:

["Conversation"]

["Vision","Conversation"]

["Math","Conversation"]

User:

{request}
"""

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": self._model,
                "prompt": prompt,
                "format": "json",
                "stream": False,
                "options": {
                    "temperature": 0,
                },
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        try:

            payload = json.loads(
                data["response"]
            )

            #
            # Model returned:
            #
            # ["Vision","Conversation"]
            #

            if isinstance(
                payload,
                list,
            ):

                return payload

            #
            # Model returned:
            #
            # {"tools":[...]}
            #

            if (
                isinstance(payload, dict)
                and "tools" in payload
            ):

                return payload["tools"]

        except Exception:

            pass

        return [
            "Conversation"
        ]