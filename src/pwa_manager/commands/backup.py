"""
PWA Manager.

Backup command.
"""

from ..context import get_apps
from ..backup import create_backup



def run():

    return create_backup(
        get_apps()
    )
