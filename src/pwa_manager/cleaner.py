"""
PWA Manager Cleaner.

Detects duplicate PWA desktop entries.
"""

from pathlib import Path


APPLICATIONS_DIR = (
    Path.home()
    / ".local/share/applications"
)


def find_duplicates(apps):

    groups = {}


    for app in apps:

        name = app.normalized_name

        if name not in groups:

            groups[name] = []


        groups[name].append(app)


    duplicates = []


    for name, items in groups.items():

        if len(items) > 1:

            duplicates.append(
                items
            )


    return duplicates



def run_clean(apps):

    print(
        "PWA Manager Clean"
    )

    print(
        "================="
    )

    print()


    duplicates = find_duplicates(
        apps
    )


    if not duplicates:

        print(
            "No duplicates found."
        )

        return


    print(
        "Duplicates found:"
    )


    for group in duplicates:

        print()


        print(
            group[0].display_name
        )


        managed = [
            app
            for app in group
            if app.source == "managed"
        ]


        chrome = [
            app
            for app in group
            if app.source == "chrome"
        ]


        if managed:

            print()

            print(
                " Keep:"
            )

            for app in managed:

                print(
                    f"   {app.desktop_file.name}"
                )


        if chrome:

            print()

            print(
                " Candidate:"
            )

            for app in chrome:

                print(
                    f"   {app.desktop_file.name}"
                )
