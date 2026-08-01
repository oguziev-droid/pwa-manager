"""
PWA Manager.

Clean command.
"""

from ..context import get_apps
from ..cleaner import run_clean
from ..clean_fix import run_clean_fix



def run(fix=False):

    apps = get_apps()

    if fix:

        return run_clean_fix(
            apps
        )

    return run_clean(
        apps
    )
