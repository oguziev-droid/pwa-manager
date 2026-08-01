from pathlib import Path

from .models import PWAApplication


APPLICATIONS_DIR = Path.home() / ".local/share/applications"


def scan_pwa() -> list[PWAApplication]:
    """
    Find Chrome generated PWA desktop files.
    """

    applications = []

    for desktop in APPLICATIONS_DIR.glob(
        "com.google.Chrome.flextop*.desktop"
    ):
        name = None
        icon = None

        for line in desktop.read_text(
            encoding="utf-8"
        ).splitlines():

            if line.startswith("Name="):
                name = line.replace(
                    "Name=", ""
                )

            if line.startswith("Icon="):
                icon = line.replace(
                    "Icon=", ""
                )

        if name:
            applications.append(
                PWAApplication(
                    name=name,
                    desktop_file=desktop,
                    icon=icon,
                    source="chrome",
                    app_type="pwa",
               )
            )

    return applications
