"""
PWA Manager Backup.

Creates backups of PWA desktop files and icons.
"""

from pathlib import Path
from datetime import datetime
import shutil

from .icons import find_icon



BACKUP_ROOT = (
    Path.home()
    /
    ".local/share/pwa-manager/backups"
)



def create_backup(apps):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    backup_dir = (
        BACKUP_ROOT
        /
        timestamp
    )


    applications_dir = (
        backup_dir
        /
        "applications"
    )


    icons_dir = (
        backup_dir
        /
        "icons"
    )


    applications_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    icons_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    print(
        "PWA Manager Backup"
    )

    print(
        "=================="
    )

    print()

    print(
        "Backup location:"
    )

    print(
        backup_dir
    )



    copied_apps = 0
    copied_icons = 0



    for app in apps:


        desktop = Path(
            app.desktop_file
        )


        if desktop.exists():

            shutil.copy2(
                desktop,
                applications_dir / desktop.name
            )

            copied_apps += 1



        found_icon = find_icon(
            app.icon
        )


        if found_icon:

            shutil.copy2(
                found_icon,
                icons_dir / found_icon.name
            )

            copied_icons += 1



    print()

    print(
        f"Desktop files: {copied_apps}"
    )

    print(
        f"Icons: {copied_icons}"
    )

    print()

    print(
        "Backup completed."
    )

    return backup_dir
