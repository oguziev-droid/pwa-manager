"""
PWA Manager Doctor Command.
"""

from ..doctor import run_doctor


def run(apps):

    return run_doctor(
        apps
    )