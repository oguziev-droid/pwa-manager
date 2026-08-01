"""
PWA Manager.

Export command.
"""

from ..context import get_apps
from ..exporter import create_export



def run():

    return create_export(
        get_apps()
    )
