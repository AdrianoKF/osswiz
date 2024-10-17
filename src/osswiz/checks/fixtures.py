from importlib.abc import Traversable
from pathlib import Path


def license_files(root: Traversable) -> list[Path]:
    """Identify common license files in the repository"""
    prefixes = ("LICENSE", "COPYING")
    return [f for f in root.iterdir() if f.name.startswith(prefixes)]
