"""
PWA Manager.

Clean command.
"""

from ..cleaner import run_clean
from ..clean_fix import run_clean_fix


def run(apps, fix=False):

    if fix:

        return run_clean_fix(
            apps
        )

    return run_clean(
        apps
    )