"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/ollama_provider.py

Purpose:
    Ollama AI Provider

Foundation Release:
    21.2
==========================================================
"""

from __future__ import annotations

import json
import time
from collections.abc import Iterator

import requests

from .models import AIResponse
from .provider import AIProvider


class OllamaProvider(AIProvider):

    def __init__(
        self,
        model: str = "qwen3:8b",
    ) -> None:

        self._model = model

    @property
    def name(self) -> str:

        return "Ollama"

    def _request_payload(
        self,
        prompt: str,
        stream: bool,
    ) -> dict:

        return {
            "model": self._model,
            "prompt": prompt,
            "stream": stream,
            "options": {

                "temperature": 0.2,

                "top_p": 0.9,

                "num_predict": 256,

                "num_ctx": 4096,

            },
        }

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:

        print()
        print("──────── AI Timing ────────")

        start = time.perf_counter()

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json=self._request_payload(
                prompt,
                stream=False,
            ),
            timeout=300,
        )

        elapsed = time.perf_counter() - start

        response.raise_for_status()

        data = response.json()

        print(f"Model      : {self._model}")
        print(f"Total Time : {elapsed:.2f} sec")

        if (
            "eval_count" in data
            and "eval_duration" in data
        ):

            seconds = (
                data["eval_duration"]
                / 1_000_000_000
            )

            if seconds > 0:

                print(
                    f"Tokens/sec : "
                    f"{data['eval_count']/seconds:.1f}"
                )

        print("──────────────────────────")
        print()

        #
        # Diagnostics
        #

        print("Returned keys:")

        print(sorted(data.keys()))

        print()

        message = data.get(
            "response",
            "",
        ).strip()

        if not message:

            print(
                "WARNING: Empty response returned."
            )

            print()

            print(
                json.dumps(
                    data,
                    indent=2,
                )
            )

        return AIResponse(
            message=message,
            provider=self.name,
            success=True,
        )

    def stream(
        self,
        prompt: str,
    ) -> Iterator[str]:

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json=self._request_payload(
                prompt,
                stream=True,
            ),
            stream=True,
            timeout=300,
        )

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            payload = json.loads(
                line.decode("utf-8")
            )

            if payload.get(
                "response"
            ):

                yield payload[
                    "response"
                ]

            if payload.get(
                "done",
                False,
            ):
                break