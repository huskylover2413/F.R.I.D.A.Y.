"""
==========================================================
F.R.I.D.A.Y.

Wake Detector

Foundation Release 50.2
==========================================================
"""

from __future__ import annotations

from pathlib import Path

from openwakeword.model import Model

from .models import WakeEvent
from .models import WakeResult


class WakeDetector:
    """
    Detects FRIDAY's custom wake phrase from live audio.
    """

    def __init__(
        self,
        confidence: float = 0.50,
    ) -> None:

        self._confidence = confidence

        model_path = (
            Path(__file__).resolve().parents[2]
            / "models"
            / "wake"
            / "Hey_Friday_20260714_164709.onnx"
        )

        if not model_path.exists():

            raise FileNotFoundError(
                f"FRIDAY wake model not found: "
                f"{model_path}"
            )

        self._model = Model(
            wakeword_models=[
                str(model_path)
            ],
            inference_framework="onnx",
        )

    def detect(
        self,
        audio,
    ) -> WakeEvent:

        predictions = self._model.predict(
            audio
        )

        for name, score in predictions.items():

            if score >= self._confidence:

                return WakeEvent(
                    phrase=name,
                    result=WakeResult.WAKE,
                )

        return WakeEvent(
            phrase="",
            result=WakeResult.SLEEP,
        )