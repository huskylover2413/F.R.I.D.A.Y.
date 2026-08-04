"""
==========================================================
F.R.I.D.A.Y.
Echo Demo

Purpose:
    Demonstrates the complete speech pipeline.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from runtime.devices import MockMicrophone
from runtime.speech import (
    MockSpeechProvider,
    SpeechRecognizer,
)


def main() -> None:
    """
    Demonstrate the speech pipeline.
    """

    microphone = MockMicrophone()

    provider = MockSpeechProvider(
        microphone
    )

    recognizer = SpeechRecognizer(
        provider
    )

    result = recognizer.listen()

    print()
    print("==========================================")
    print("FRIDAY Speech Demonstration")
    print("==========================================")
    print()

    print(result.text)
    print(f"Confidence : {result.confidence:.2f}")
    print()


if __name__ == "__main__":
    main()