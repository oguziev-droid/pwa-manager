"""
PWA Manager Icons.

Common icon discovery utilities.
"""

from pathlib import Path


ICON_SEARCH_PATHS = [
    Path.home() / ".local/share/icons",
    Path.home() / ".icons",
    Path("/usr/share/icons"),
    Path("/usr/share/pixmaps"),
]


ICON_ALIASES = {
    "google-gemini": [
        "gemini.svg",
        "gemini.png",
    ],
}



def find_icon(icon):

    if not icon:

        return None


    icon_path = Path(icon)


    # Direct file path

    if icon_path.exists():

        return icon_path



    icon_name = icon_path.name


    base_name = icon_name


    if "." in base_name:

        base_name = base_name.rsplit(
            ".",
            1
        )[0]



    possible_names = [
        icon_name,
        base_name,
        base_name + ".png",
        base_name + ".svg",
        base_name + ".svgz",
    ]



    if base_name in ICON_ALIASES:

        possible_names.extend(
            ICON_ALIASES[base_name]
        )



    # Exact search

    for directory in ICON_SEARCH_PATHS:

        if not directory.exists():

            continue


        try:

            for file in directory.rglob("*"):

                if file.name in possible_names:

                    return file


        except PermissionError:

            continue



    # Partial search

    for directory in ICON_SEARCH_PATHS:

        if not directory.exists():

            continue


        try:

            for file in directory.rglob("*"):

                if base_name in file.name:

                    return file


        except PermissionError:

            continue



    return None
