"""
==========================================================
F.R.I.D.A.Y.

Apple Speech File Demo
==========================================================
"""

from runtime.platforms.apple.speech_file import (
    AppleSpeechFileRecognizer,
)


def main() -> None:

    recognizer = AppleSpeechFileRecognizer()

    print()
    print("=========================================")
    print(" Apple Speech File Recognition Demo")
    print("=========================================")
    print()

    filename = input(
        "Audio file: "
    ).strip()

    print()

    result = recognizer.recognize(filename)

    print("Recognized:")
    print(result)
    print()


if __name__ == "__main__":
    main()