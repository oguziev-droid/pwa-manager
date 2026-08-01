"""
PWA Manager Doctor.

Checks PWA installation health.
"""

from pathlib import Path


def check_desktop_file(app):

    return Path(app.desktop_file).exists()


def check_icon(app):

    if not app.icon:
        return False, "missing"

    icon = str(app.icon)

    # Реальний файл
    if icon.startswith("/"):
        path = Path(icon)

        if path.exists():
            return True, "file"

        # пошук SVG/PNG в каталогах іконок
        if path.suffix in [".svg", ".png"]:

            if "icons" in path.parts:
                return True, "theme"

        return False, "missing file"


    # Chrome PWA
    if icon.startswith("chrome-"):
        return True, "chrome"


    # Системна назва іконки
    return True, "theme"


def check_exec(app):

    try:

        content = Path(app.desktop_file).read_text()

        for line in content.splitlines():

            if line.startswith("Exec="):
                return True

    except Exception:
        pass

    return False


def run_doctor(apps):

    print("PWA Manager Doctor")
    print("==================")

    for app in apps:

        print(
            f"\n{app.display_name}"
        )

        desktop = check_desktop_file(app)
        exec_ok = check_exec(app)
        icon_ok, icon_type = check_icon(app)


        print(
            "  Desktop:",
            "OK" if desktop else "ERROR"
        )

        print(
            "  Exec:",
            "OK" if exec_ok else "ERROR"
        )


        if icon_ok:

            labels = {
                "file": "OK (file)",
                "theme": "OK (theme)",
                "chrome": "OK (chrome)",
            }

            print(
                "  Icon:",
                labels.get(icon_type, "OK")
            )

        else:

            print(
                "  Icon: ERROR"
            )
