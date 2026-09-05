"""
PWA Manager.

Command dispatcher.
"""

import sys


from .context import get_apps

from .commands.list import run as list_command
from .commands.doctor import run as doctor_command
from .commands.status import run as status_command
from .commands.repair import run as repair_command
from .commands.backup import run as backup_command
from .commands.clean import run as clean_command
from .commands.restore import run as restore_command
from .commands.export import run as export_command
from .commands.icons import run as icons_command


COMMANDS = {

    "list": list_command,

    "doctor": doctor_command,

    "status": status_command,

    "repair": repair_command,

    "backup": backup_command,

    "clean": clean_command,

    "restore": restore_command,

    "export": export_command,

    "icons": icons_command,

}



def print_help():

    print(
        "PWA Manager v0.1.0"
    )

    print()

    print(
        "Commands:"
    )

    print(
        "  list"
    )

    print(
        "  doctor"
    )

    print(
        "  status"
    )

    print(
        "  repair"
    )

    print(
        "  backup"
    )

    print(
        "  restore <backup>"
    )

    print(
        "  export"
    )

    print(
        "  clean"
    )

    print(
        "  clean --fix"
    )

    print(
        "  icons"
    )

    print(
        "  icons --fix"
    )


def dispatch():

    if len(sys.argv) < 2:

        print_help()

        return


    command = sys.argv[1]


    apps = get_apps()



    if command == "clean":

        fix = (
            len(sys.argv) > 2
            and sys.argv[2] == "--fix"
        )

        return clean_command(
            apps,
            fix=fix
        )



    if command == "icons":

        fix = (
            len(sys.argv) > 2
            and sys.argv[2] == "--fix"
        )

        return icons_command(
            apps,
            fix=fix
        )



    if command == "restore":

        if len(sys.argv) < 3:

            print(
                "Usage: restore <backup>"
            )

            return


        return restore_command(
            sys.argv[2]
        )



    handler = COMMANDS.get(
        command
    )


    if handler:

        return handler(
            apps
        )


    print_help()
