"""
PWA Manager ZIP utilities.

Creates ZIP archives for exported PWA packages.
"""

from pathlib import Path
import shutil


def create_zip(folder: Path) -> Path:
    """
    Create ZIP archive from exported folder.

    Returns:
        Path to created ZIP archive.
    """

    archive = shutil.make_archive(
        base_name=str(folder),
        format="zip",
        root_dir=folder.parent,
        base_dir=folder.name,
    )

    return Path(archive)
