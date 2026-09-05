"""
PWA Manager Doctor.

Checks PWA installation health.
"""

from pathlib import Path


def check_desktop_file(app):

    return Path(
        app.desktop_file
    ).exists()


def check_icon(app):

    if not app.icon:

        return False, "missing"


    icon = str(
        app.icon
    )


    # Absolute path to an icon file.

    if icon.startswith("/"):

        path = Path(
            icon
        )


        if path.exists():

            return True, "file"


        return False, "missing"


    # Chrome-generated PWA icon.

    if icon.startswith("chrome-"):

        return True, "chrome"


    # Icon name from an installed icon theme.

    return True, "theme"


def check_exec(app):

    try:

        content = Path(
            app.desktop_file
        ).read_text(
            encoding="utf-8"
        )


        for line in content.splitlines():

            if line.startswith("Exec="):

                return True


    except Exception:

        pass


    return False


def run_doctor(apps):

    print(
        "PWA Manager Doctor"
    )

    print(
        "=================="
    )


    for app in apps:

        print()

        print(
            app.display_name
        )


        desktop_ok = (
            check_desktop_file(
                app
            )
        )


        exec_ok = (
            check_exec(
                app
            )
        )


        icon_ok, icon_type = (
            check_icon(
                app
            )
        )


        print(
            "  Desktop:",
            "OK"
            if desktop_ok
            else "ERROR"
        )


        print(
            "  Exec:",
            "OK"
            if exec_ok
            else "ERROR"
        )


        if icon_ok:

            labels = {

                "file":
                    "OK (file)",

                "theme":
                    "OK (theme)",

                "chrome":
                    "OK (chrome)",

            }


            print(
                "  Icon:",
                labels.get(
                    icon_type,
                    "OK"
                )
            )


        else:

            print(
                "  Icon: ERROR"
            )