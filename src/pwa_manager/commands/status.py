"""
PWA Manager.

Status command.
"""

from ..context import get_apps
from ..status import run_status



def run():

    return run_status(
        get_apps()
    )
