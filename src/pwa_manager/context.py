"""
PWA Manager.

Shared application context.
"""

from .scanner import scan_pwa
from .managed_scanner import scan_managed_pwa
from .deduplicator import deduplicate
from .classifier import classify


def get_apps():
    """
    Scan the system, merge all discovered PWA applications,
    classify them and return a ready-to-use list.
    """

    apps = deduplicate(
        scan_pwa()
        +
        scan_managed_pwa()
    )

    for app in apps:
        app.app_type = classify(app)

    return apps
