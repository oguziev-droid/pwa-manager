"""
PWA Manager.

Repair command.
"""

from ..repair import run_repair


def run(apps):

    return run_repair(
        apps
    )