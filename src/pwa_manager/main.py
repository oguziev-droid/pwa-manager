"""
PWA Manager.

Main application entry point.
"""

import sys

from .dispatcher import dispatch


VERSION = "0.1.0"



def print_help():

    print(
        f"PWA Manager v{VERSION}"
    )

    print()

    print(
        "Usage:"
    )

    print(
        "  pwa-manager <command>"
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

    print()

    print(
        "Options:"
    )

    print(
        "  -h, --help       Show this help"
    )

    print(
        "  --version        Show version"
    )



def main():

    if len(sys.argv) > 1:

        if sys.argv[1] in (
            "-h",
            "--help"
        ):

            print_help()

            return


        if sys.argv[1] == "--version":

            print(
                f"PWA Manager v{VERSION}"
            )

            return



    dispatch()



if __name__ == "__main__":

    main()
