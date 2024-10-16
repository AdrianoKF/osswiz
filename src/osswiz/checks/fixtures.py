from os import PathLike
from pathlib import Path


def license_files(root: str | PathLike[str]) -> list[Path]:
    """Identify common license files in the repository"""

    return list(Path(root).glob("LICENSE*")) + list(Path(root).glob("COPYING*"))
