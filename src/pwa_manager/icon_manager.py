"""
PWA Manager Icon Manager.

Analyzes and repairs application icons.
"""

from pathlib import Path
import re
import shutil


ICON_STORAGE = (
    Path.home()
    / ".local/share/pwa-manager/icons"
)


ICON_STORAGE.mkdir(
    parents=True,
    exist_ok=True
)


DESKTOP_ICON_PATTERN = re.compile(
    r"^Icon=.*$",
    re.MULTILINE
)


def detect_icon_type(icon):

    if not icon:
        return "missing"


    icon = str(icon)


    if icon.startswith("/"):
        path = Path(icon)

        if path.exists():

            if path.suffix in [
                ".png",
                ".svg",
                ".svgz",
            ]:
                return "file"

            return "file"


        return "missing file"


    if icon.startswith("chrome-"):

        return "chrome"


    return "theme"



def analyze_icons(apps):

    print(
        "PWA Manager Icons"
    )

    print(
        "================="
    )

    print()


    for app in apps:

        icon_type = detect_icon_type(
            app.icon
        )


        print(
            app.display_name
        )

        print(
            f"  Icon: {app.icon}"
        )

        print(
            f"  Type: {icon_type}"
        )

        print()



def find_replacement_icon(app):

    if not app.icon:
        return None


    icon = Path(
        app.icon
    )


    if icon.exists():

        return icon


    return None



def update_desktop_icon(app, icon_path):

    # Rewrite the Icon= line in the .desktop file so it
    # points at the centrally-managed icon copy instead
    # of whatever theme/path it used before.

    desktop_file = Path(
        app.desktop_file
    )


    if not desktop_file.exists():

        return False


    content = desktop_file.read_text()


    new_line = f"Icon={icon_path}"


    if new_line in content:

        # Already pointing at the right icon, nothing to do.

        return False


    if not DESKTOP_ICON_PATTERN.search(content):

        # No Icon= line present, don't guess where to insert it.

        return False


    new_content = DESKTOP_ICON_PATTERN.sub(
        new_line,
        content,
        count=1,
    )


    desktop_file.write_text(
        new_content
    )


    return True



def repair_icons(apps):

    print(
        "PWA Manager Icon Repair"
    )

    print(
        "======================"
    )

    print()


    prepared = 0

    applied = 0


    for app in apps:

        source = find_replacement_icon(
            app
        )


        if not source:
            continue


        destination = (
            ICON_STORAGE
            /
            source.name
        )


        if not destination.exists():

            shutil.copy2(
                source,
                destination
            )


        prepared += 1


        changed = update_desktop_icon(
            app,
            destination
        )


        if changed:

            applied += 1

            print(
                f"{app.display_name}: {destination}  (desktop file updated)"
            )

        else:

            print(
                f"{app.display_name}: {destination}  (already up to date)"
            )


    print()

    print(
        f"Icons prepared: {prepared}"
    )

    print(
        f"Desktop files updated: {applied}"
    )