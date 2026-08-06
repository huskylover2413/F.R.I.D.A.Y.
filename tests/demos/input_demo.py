"""
==========================================================
F.R.I.D.A.Y.

Input Demonstration
==========================================================
"""

from runtime.input import KeyboardInput


def main() -> None:

    keyboard = KeyboardInput()

    print()
    print("==========================================")
    print("FRIDAY Input Demonstration")
    print("==========================================")
    print()

    text = keyboard.read()

    print()
    print(f'You entered: "{text}"')
    print()


if __name__ == "__main__":
    main()