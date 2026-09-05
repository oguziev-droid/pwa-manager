"""
PWA Manager Icons command.

Shows and repairs application icons.
"""

from ..icon_manager import (
    analyze_icons,
    repair_icons,
)


def run(apps, fix=False):

    if fix:

        repair_icons(apps)

    else:

        analyze_icons(apps)
