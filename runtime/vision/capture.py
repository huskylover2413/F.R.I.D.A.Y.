"""
==========================================================
F.R.I.D.A.Y.
Screen Capture Provider

Foundation Release:
    20.3
==========================================================
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from PIL import ImageGrab

from .models import ScreenCapture


class ScreenCaptureProvider:

    def capture(
        self,
    ) -> ScreenCapture:

        image = ImageGrab.grab()

        output = (
            Path.home()
            / "Pictures"
            / "FRIDAY"
        )

        output.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.png"
        )

        path = output / filename

        image.save(path)

        return ScreenCapture(
            path=path,
            image=path.read_bytes(),
            width=image.width,
            height=image.height,
            created=datetime.now(),
        )