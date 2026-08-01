"""
PWA Manager Repair.

Checks and prepares repair actions.
"""

from .doctor import (
    check_desktop_file,
    check_icon,
    check_exec,
)


def run_repair(apps):

    print(
        "PWA Manager Repair"
    )

    print(
        "=================="
    )


    for app in apps:

        desktop_ok = check_desktop_file(app)
        exec_ok = check_exec(app)
        icon_ok, icon_type = check_icon(app)


        print(
            f"\n{app.display_name}"
        )


        problems = []


        if not desktop_ok:
            problems.append(
                "missing desktop file"
            )


        if not exec_ok:
            problems.append(
                "invalid Exec"
            )


        if not icon_ok:
            problems.append(
                "missing icon"
            )


        if problems:

            print(
                "  Status: NEEDS REPAIR"
            )

            for problem in problems:

                print(
                    f"   - {problem}"
                )

        else:

            print(
                "  Status: HEALTHY"
            )
