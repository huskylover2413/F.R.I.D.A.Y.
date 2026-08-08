"""
==========================================================
F.R.I.D.A.Y.
Gemma Vision Provider

Foundation Release 22.3
==========================================================
"""

from __future__ import annotations

import base64
from pathlib import Path

import requests

from .base import VisionProvider


class GemmaVisionProvider(VisionProvider):

    def describe(
        self,
        image: Path,
        prompt: str,
    ) -> str:

        #
        # Read image and convert to Base64
        #
        with open(image, "rb") as f:

            image_data = base64.b64encode(
                f.read()
            ).decode("utf-8")

        payload = {

            "model": "gemma3:4b",

            "messages": [

                {

                    "role": "user",

                    "content": prompt,

                    "images": [
                        image_data
                    ],

                }

            ],

            "stream": False,

        }

        response = requests.post(
            "http://127.0.0.1:11434/api/chat",
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return (
            data["message"]["content"]
            .strip()
        )