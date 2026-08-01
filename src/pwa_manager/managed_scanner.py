from pathlib import Path

from .models import PWAApplication


APPLICATIONS_DIR = Path.home() / ".local/share/applications"


def scan_managed_pwa() -> list[PWAApplication]:
    """
    Find PWA Manager created desktop files.
    """

    applications = []

    for desktop in APPLICATIONS_DIR.glob("*.desktop"):

        # Наші файли мають прості назви
        # і не починаються з com.google.Chrome
        if desktop.name.startswith(
            "com.google.Chrome"
        ):
            continue

        name = None
        icon = None

        content = desktop.read_text(
            encoding="utf-8"
        ).splitlines()

        for line in content:

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
                    source="managed",
                    app_type="pwa",
                )
            )

    return applications
