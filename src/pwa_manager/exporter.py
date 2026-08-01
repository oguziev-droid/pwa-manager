"""
PWA Manager Export.

Creates portable backup package.
"""

from pathlib import Path
from datetime import datetime
import shutil
import json

from .icons import find_icon



EXPORT_DIR = (
    Path.home()
    / ".local/share/pwa-manager/exports"
)


EXPORT_VERSION = "1.0"



def create_export(apps):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    export_path = (
        EXPORT_DIR
        /
        f"PWA-Backup-{timestamp}"
    )


    applications_dir = (
        export_path
        /
        "applications"
    )


    icons_dir = (
        export_path
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


    desktop_count = 0
    icon_count = 0


    config = {
        "version": EXPORT_VERSION,
        "applications": []
    }



    for app in apps:


        desktop = Path(
            app.desktop_file
        )


        if desktop.exists():

            shutil.copy2(
                desktop,
                applications_dir / desktop.name
            )

            desktop_count += 1



        icon_name = None


        found_icon = find_icon(
            app.icon
        )


        if found_icon:

            icon_name = found_icon.name


            shutil.copy2(
                found_icon,
                icons_dir / icon_name
            )

            icon_count += 1



        config["applications"].append(
            {
                "name": app.display_name,
                "source": app.source,
                "type": app.app_type,
                "desktop": desktop.name,
                "icon": icon_name
            }
        )



    with open(
        export_path / "config.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            config,
            file,
            indent=2,
            ensure_ascii=False
        )



    print(
        "PWA Manager Export"
    )

    print(
        "=================="
    )

    print()

    print(
        "Export location:"
    )

    print(
        export_path
    )

    print()

    print(
        f"Desktop files: {desktop_count}"
    )

    print(
        f"Icons: {icon_count}"
    )

    print()

    print(
        "Portable configuration: OK"
    )

    print()

    print(
        "Export completed."
    )
