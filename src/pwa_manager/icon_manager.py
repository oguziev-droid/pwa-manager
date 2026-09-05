"""
PWA Manager Icon Manager.

Analyzes and repairs application icons.
"""

from pathlib import Path
import re
import shutil

from .icons import find_icon


ICON_STORAGE = (
    Path.home()
    / ".local/share/pwa-manager/icons"
)


ICON_STORAGE.mkdir(
    parents=True,
    exist_ok=True
)


DESKTOP_DIRS = [
    Path.home() / ".local/share/applications",
    Path.home() / "Desktop",
]


DESKTOP_ICON_PATTERN = re.compile(
    r"^Icon=.*$",
    re.MULTILINE
)


APP_ID_PATTERN = re.compile(
    r"chrome-([a-z]+)-Default"
)


def detect_icon_type(icon):

    if not icon:
        return "missing"

    icon = str(icon)

    if icon.startswith("/"):
        path = Path(icon)

        if path.exists():
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



def resolve_real_icon(app):
    """
    Find the actual icon file for an app, regardless of
    whether its current Icon= value is a direct path or
    a theme name (e.g. chrome-<id>-Default).
    """

    if not app.icon:
        return None

    icon_path = Path(app.icon)

    if icon_path.exists():
        return icon_path

    # Theme-name style icon (e.g. "chrome-<id>-Default")
    # search standard icon directories for a real file.

    return find_icon(app.icon)



def extract_app_id(desktop_file):

    match = APP_ID_PATTERN.search(
        desktop_file.name
    )

    if not match:
        return None

    return match.group(1)



def find_sibling_desktop_files(app_id):
    """
    Find every .desktop file across managed locations
    (applications dir + Desktop) that refers to the same
    Chrome app-id, so all copies get fixed together.
    """

    if not app_id:
        return []

    matches = []

    for directory in DESKTOP_DIRS:

        if not directory.exists():
            continue

        for desktop in directory.glob(f"*{app_id}*.desktop"):
            matches.append(desktop)

    return matches



def update_desktop_icon(desktop_file, icon_path):

    if not desktop_file.exists():
        return False

    content = desktop_file.read_text()

    new_line = f"Icon={icon_path}"

    if new_line in content:
        return False

    if not DESKTOP_ICON_PATTERN.search(content):
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

        source = resolve_real_icon(app)

        if not source:
            continue

        # Centralize a copy for our own bookkeeping,
        # but always point Icon= at an absolute file path
        # (theme-name lookups are unreliable across
        # different desktop shells/extensions).

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

        # Fix the icon everywhere the same app-id appears:
        # applications dir AND Desktop, if present.

        app_id = extract_app_id(app.desktop_file)

        targets = find_sibling_desktop_files(app_id) if app_id else [app.desktop_file]

        if app.desktop_file not in targets:
            targets.append(app.desktop_file)

        changed_any = False

        for target in targets:

            changed = update_desktop_icon(
                target,
                source
            )

            if changed:
                changed_any = True

        if changed_any:
            applied += 1

            print(
                f"{app.display_name}: {source}  (desktop file(s) updated)"
            )

        else:

            print(
                f"{app.display_name}: {source}  (already up to date)"
            )

    print()

    print(
        f"Icons prepared: {prepared}"
    )

    print(
        f"Desktop files updated: {applied}"
    )