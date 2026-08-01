"""
PWA Manager Status.

Shows summary information about PWA health.
"""

from .doctor import (
    check_desktop_file,
    check_icon,
    check_exec,
)


def run_status(apps):

    total = len(apps)

    healthy = 0
    warnings = 0
    errors = 0

    icon_types = {
        "file": 0,
        "theme": 0,
        "chrome": 0,
    }


    for app in apps:

        desktop_ok = check_desktop_file(app)

        exec_ok = check_exec(app)

        icon_ok, icon_type = check_icon(app)


        if icon_type in icon_types:
            icon_types[icon_type] += 1


        if (
            desktop_ok
            and exec_ok
            and icon_ok
        ):
            healthy += 1

        elif icon_ok:
            warnings += 1

        else:
            errors += 1


    print(
        "PWA Manager Status"
    )

    print(
        "=================="
    )

    print()

    print(
        f"Applications: {total}"
    )

    print(
        f"Healthy: {healthy}"
    )

    print(
        f"Warnings: {warnings}"
    )

    print(
        f"Errors: {errors}"
    )


    print()

    print(
        "Icons:"
    )

    print(
        f"  File: {icon_types['file']}"
    )

    print(
        f"  Theme: {icon_types['theme']}"
    )

    print(
        f"  Chrome: {icon_types['chrome']}"
    )
