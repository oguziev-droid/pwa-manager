"""
PWA Manager.

Restore command.
"""

from ..restore import restore_backup



def run(name):

    return restore_backup(
        name
    )
