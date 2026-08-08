"""
==========================================================
F.R.I.D.A.Y.
OCR Engine

Foundation Release 20.3
==========================================================
"""

from __future__ import annotations

from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


class OCREngine:

    def __init__(self) -> None:

        self._engine = RapidOCR()

    def read(
        self,
        image_path: Path,
    ) -> str:

        result, _ = self._engine(
            str(image_path)
        )

        if not result:
            return ""

        return "\n".join(
            item[1]
            for item in result
        )