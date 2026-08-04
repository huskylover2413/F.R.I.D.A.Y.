"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    builder/forge.py

Purpose:
    Forge is the engineering platform responsible for
    verifying and eventually building the FRIDAY project.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.2 - Forge
==========================================================
"""

from runtime.console import console
from builder.project import verify_project
from builder.blueprint import PROJECT_NAME


def display_results() -> bool:
    """
    Verify the project and display the results.

    Returns:
        True if the project is healthy.
        False otherwise.
    """

    status = verify_project()

    console.header("Forge")

    console.system(f"Project : {PROJECT_NAME}")
    console.system("Version : Alpha 0.2 - Forge")
    console.info("Beginning project verification...")
    print()

    console.info("Checking folders")

    for folder in status.folders:
        if folder.exists:
            console.success(str(folder.path))
        else:
            console.error(f"Missing folder: {folder.path}")

    print()

    console.info("Checking files")

    for file in status.files:
        if file.exists:
            console.success(str(file.path))
        else:
            console.error(f"Missing file: {file.path}")

    print()

    if status.healthy:
        console.success("Project Healthy")
        console.system("FRIDAY is ready for development.")
    else:
        console.warning("Project Incomplete")
        console.system("Correct the missing items above.")

    return status.healthy


def main() -> None:
    """
    Forge application entry point.
    """

    display_results()


if __name__ == "__main__":
    main()