"""
PWA Manager.

Export command.
"""

from ..exporter import create_export


def run(apps):

    return create_export(
        apps
    )