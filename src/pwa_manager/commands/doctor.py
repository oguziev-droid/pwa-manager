"""
PWA Manager.

Doctor command.
"""

from ..doctor import run_doctor

from ..scanner import scan_pwa
from ..managed_scanner import scan_managed_pwa
from ..deduplicator import deduplicate
from ..classifier import classify



def get_apps():

    apps = deduplicate(
        scan_pwa()
        +
        scan_managed_pwa()
    )

    for app in apps:

        app.app_type = classify(app)

    return apps



def run():

    return run_doctor(
        get_apps()
    )
