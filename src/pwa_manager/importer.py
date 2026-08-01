"""
PWA Manager Import.

Restores exported PWA configuration.
"""

from pathlib import Path
import shutil
import json
import subprocess


APPLICATIONS_DIR = (
    Path.home()
    / ".local/share/applications"
)


ICONS_DIR = (
    Path.home()
    / ".local/share/pwa-manager/icons"
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



def run_import(import_path):

    source = Path(
        import_path
    )


    if not source.exists():

        print(
            "Import source not found:"
        )

        print(
            source
        )

        return


    applications = (
        source
        /
        "applications"
    )


    icons = (
        source
        /
        "icons"
    )


    config = (
        source
        /
        "config.json"
    )


    desktop_count = 0
    icon_count = 0


    if applications.exists():

        for file in applications.iterdir():

            shutil.copy2(
                file,
                APPLICATIONS_DIR
                /
                file.name
            )

            desktop_count += 1



    if icons.exists():

        ICONS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


        for file in icons.iterdir():

            shutil.copy2(
                file,
                ICONS_DIR
                /
                file.name
            )

            icon_count += 1



    config_ok = False


    if config.exists():

        with open(
            config,
            encoding="utf-8"
        ) as file:

            json.load(file)

            config_ok = True



    refresh_gnome()


    print(
        "PWA Manager Import"
    )

    print(
        "=================="
    )

    print()

    print(
        f"Desktop files restored: {desktop_count}"
    )

    print(
        f"Icons restored: {icon_count}"
    )

    print()

    if config_ok:

        print(
            "Configuration: OK"
        )

    print()

    print(
        "Import completed."
    )
