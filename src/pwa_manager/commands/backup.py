"""
PWA Manager.

Backup command.
"""

from ..backup import create_backup


def run(apps):

    return create_backup(
        apps
    )