"""
PWA Manager Clean Fix.

Removes duplicate Chrome PWA desktop files.
"""

from pathlib import Path
import subprocess


APPLICATIONS_DIR = (
    Path.home()
    / ".local/share/applications"
)


def remove_chrome_duplicate(app):

    desktop = Path(
        app.desktop_file
    )


    if (
        app.source == "chrome"
        and desktop.exists()
    ):

        desktop.unlink()

        return True


    return False



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



def run_clean_fix(apps):

    print(
        "PWA Manager Clean Fix"
    )

    print(
        "===================="
    )

    print()


    removed = 0


    groups = {}


    for app in apps:

        name = app.normalized_name

        groups.setdefault(
            name,
            []
        ).append(app)


    for name, items in groups.items():

        if len(items) <= 1:

            continue


        managed = [
            app
            for app in items
            if app.source == "managed"
        ]


        chrome = [
            app
            for app in items
            if app.source == "chrome"
        ]


        print(
            items[0].display_name
        )


        for app in chrome:

            if managed:

                if remove_chrome_duplicate(app):

                    print(
                        f"  Removed: {app.desktop_file.name}"
                    )

                    removed += 1


    refresh_gnome()


    print()

    print(
        f"Clean completed. Removed: {removed}"
    )
