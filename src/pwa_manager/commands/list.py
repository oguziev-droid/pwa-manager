"""
PWA Manager.

List command.
"""

from ..context import get_apps


def run():

    apps = get_apps()

    print(
        f"Found {len(apps)} PWA applications:"
    )

    for app in apps:

        print(
            f"\n{app.display_name}"
        )

        print(
            f"  Desktop: {app.desktop_file}"
        )

        print(
            f"  Source: {app.source}"
        )

        print(
            f"  Icon: {app.icon}"
        )
