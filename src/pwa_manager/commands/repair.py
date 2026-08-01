"""
PWA Manager.

Repair command.
"""

from ..context import get_apps
from ..repair import run_repair



def run():

    return run_repair(
        get_apps()
    )
