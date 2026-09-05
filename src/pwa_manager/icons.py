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


# Chrome always writes PWA icons into the hicolor theme
# at these specific sizes. Checking them directly is far
# faster than a recursive scan of every icon theme on disk,
# and covers the overwhelming majority of real cases.

HICOLOR_SIZES = [
    "512x512",
    "256x256",
    "128x128",
    "96x96",
    "64x64",
    "48x48",
    "32x32",
    "16x16",
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



    # Fast path: hicolor theme, largest size first.
    # This is where Chrome actually stores PWA icons,
    # so it resolves almost every real-world case
    # without touching the slow recursive search below.

    hicolor = Path.home() / ".local/share/icons/hicolor"

    if hicolor.exists():

        for size in HICOLOR_SIZES:

            for name in possible_names:

                candidate = (
                    hicolor
                    / size
                    / "apps"
                    / name
                )

                if candidate.exists():

                    return candidate



    # Exact search (slow path, full recursive scan)

    for directory in ICON_SEARCH_PATHS:

        if not directory.exists():

            continue


        try:

            for file in directory.rglob("*"):

                if file.name in possible_names:

                    return file


        except PermissionError:

            continue



    # Partial search (slowest, last resort)

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
