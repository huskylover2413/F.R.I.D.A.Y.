"""
==========================================================
F.R.I.D.A.Y.

Developer Console

Foundation Release 20.1
==========================================================
"""

from __future__ import annotations

from developer.snapshot import run as snapshot


def header() -> None:

    print()
    print("══════════════════════════════════════")
    print("       F.R.I.D.A.Y. Developer")
    print("══════════════════════════════════════")
    print()


def menu() -> str:

    print("1. Brain")
    print("2. Memory")
    print("3. Vision")
    print("4. Planner")
    print("5. Reasoning")
    print("6. Status")
    print("7. Project Snapshot")
    print("8. Health Check")
    print("9. Run Everything")
    print("0. Exit")
    print()

    return input("Selection: ").strip()


def main() -> None:

    while True:

        header()

        choice = menu()

        print()

        if choice == "0":
            print("Goodbye.")
            break

        elif choice == "7":
            snapshot()

        else:
            print("Coming soon.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()