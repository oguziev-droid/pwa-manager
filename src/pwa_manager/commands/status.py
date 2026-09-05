"""
PWA Manager Status Command.
"""

from ..status import run_status


def run(apps):

    return run_status(
        apps
    )