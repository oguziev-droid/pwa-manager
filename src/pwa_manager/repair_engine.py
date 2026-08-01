"""
PWA Manager Repair Engine.

Automatic repair functions.
"""

from pathlib import Path
import subprocess

from .doctor import (
    check_desktop_file,
    check_exec,
    check_icon,
)


APPLICATIONS_DIR = (
    Path.home()
    / ".local/share/applications"
)


def refresh_gnome():

    try:

        subprocess.run(
            [
                "update-desktop-database",
                str(APPLICATIONS_DIR)
            ],
            check=False
        )

    except Exception:

        pass



def run_fix(apps):

    print(
        "PWA Manager Repair Fix"
    )

    print(
        "====================="
    )


    issues = 0


    for app in apps:

        print()

        print(
            app.display_name
        )


        desktop_ok = check_desktop_file(app)

        exec_ok = check_exec(app)

        icon_ok, icon_type = check_icon(app)


        problems = []


        if not desktop_ok:

            problems.append(
                "desktop file"
            )


        if not exec_ok:

            problems.append(
                "Exec"
            )


        if not icon_ok:

            problems.append(
                "icon"
            )


        if problems:

            print(
                "  WARNING - repair needed"
            )

            for problem in problems:

                print(
                    f"   - {problem}"
                )

            issues += 1


        else:

            print(
                "  OK - no repair needed"
            )


    refresh_gnome()


    print()

    print(
        f"Repair completed. Issues: {issues}"
    )
