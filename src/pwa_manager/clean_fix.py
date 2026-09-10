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


DESKTOP_DIR = (
    Path.home()
    / "Desktop"
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



def is_flatpak_ghost(desktop_file):
    """
    Chrome periodically re-syncs old PWA entries from the
    Google account and writes them as
    com.google.Chrome.flextop*.desktop files with an
    Exec= line pointing at a Flatpak Chrome install.
    On this system Flatpak Chrome does not exist, so any
    file matching this exact signature is a stale ghost,
    never a real, launchable app.
    """

    if not desktop_file.name.startswith(
        "com.google.Chrome.flextop"
    ):

        return False


    try:

        content = desktop_file.read_text(
            encoding="utf-8"
        )

    except OSError:

        return False


    return (
        "flatpak" in content
        and "com.google.Chrome" in content
    )



def remove_desktop_ghosts():
    """
    Scan ~/Desktop directly (not just the applications
    list) for Chrome sync ghost files and delete them.
    """

    removed = []


    if not DESKTOP_DIR.exists():

        return removed


    for desktop_file in DESKTOP_DIR.glob(
        "com.google.Chrome.flextop*.desktop"
    ):

        if is_flatpak_ghost(desktop_file):

            desktop_file.unlink()

            removed.append(
                desktop_file.name
            )


    return removed



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



    desktop_ghosts = remove_desktop_ghosts()


    if desktop_ghosts:

        print()

        print(
            "Desktop ghost files:"
        )

        for name in desktop_ghosts:

            print(
                f"  Removed: {name}"
            )


    removed += len(desktop_ghosts)


    refresh_gnome()


    print()

    print(
        f"Clean completed. Removed: {removed}"
    )