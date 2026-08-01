"""
PWA Manager Restore.

Restores PWA desktop files and icons from backup.
"""

from pathlib import Path
import shutil


BACKUP_ROOT = Path.home() / ".local/share/pwa-manager/backups"

APPLICATIONS_DIR = (
    Path.home()
    / ".local/share/applications"
)

ICONS_DIR = (
    Path.home()
    / ".local/share/pwa-manager/icons"
)


def restore_backup(name):

    backup = BACKUP_ROOT / name


    if not backup.exists():

        print(
            "Backup not found:"
        )

        print(
            backup
        )

        return


    print(
        "PWA Manager Restore"
    )

    print(
        "=================="
    )

    print()

    print(
        f"Restoring: {name}"
    )


    applications = (
        backup / "applications"
    )

    icons = (
        backup / "icons"
    )


    restored_apps = 0
    restored_icons = 0


    if applications.exists():

        for file in applications.iterdir():

            shutil.copy2(
                file,
                APPLICATIONS_DIR / file.name
            )

            restored_apps += 1


    if icons.exists():

        ICONS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


        for file in icons.iterdir():

            shutil.copy2(
                file,
                ICONS_DIR / file.name
            )

            restored_icons += 1


    print()

    print(
        f"Desktop files restored: {restored_apps}"
    )

    print(
        f"Icons restored: {restored_icons}"
    )

    print()

    print(
        "Restore completed."
    )
