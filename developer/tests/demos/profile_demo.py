"""
==========================================================
F.R.I.D.A.Y.
Profile Demo
==========================================================
"""

from runtime.profile import ProfileManager


def main() -> None:

    manager = ProfileManager()

    profile = manager.load()

    print()
    print("==========================================")
    print("FRIDAY Profile Demonstration")
    print("==========================================")
    print()

    print(f"Name      : {profile.display_name}")
    print(f"Greeting  : {profile.greeting}")
    print(f"Language  : {profile.language}")
    print(f"Voice     : {profile.voice}")
    print(f"Timezone  : {profile.timezone}")
    print()


if __name__ == "__main__":
    main()