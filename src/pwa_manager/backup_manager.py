"""
PWA Manager Backup Manager.

Lists available backups.
"""

from pathlib import Path


BACKUP_ROOT = Path.home() / ".local/share/pwa-manager/backups"


def list_backups():

    print(
        "PWA Manager Backups"
    )

    print(
        "==================="
    )

    print()


    if not BACKUP_ROOT.exists():

        print(
            "No backups found."
        )

        return


    backups = sorted(
        BACKUP_ROOT.iterdir(),
        reverse=True
    )


    if not backups:

        print(
            "No backups found."
        )

        return


    for number, backup in enumerate(
        backups,
        start=1
    ):

        applications = (
            backup / "applications"
        )

        icons = (
            backup / "icons"
        )


        app_count = 0
        icon_count = 0


        if applications.exists():

            app_count = len(
                list(
                    applications.iterdir()
                )
            )


        if icons.exists():

            icon_count = len(
                list(
                    icons.iterdir()
                )
            )


        print(
            f"{number}. {backup.name}"
        )

        print(
            f"   Applications: {app_count}"
        )

        print(
            f"   Icons: {icon_count}"
        )

        print()
