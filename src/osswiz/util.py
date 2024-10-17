import re
from collections.abc import Iterable
from typing import TypeVar


def classify_license(license_text: str) -> str | None:
    """Attempt to classify a license based on its text. Returns the SPDX identifier if recognized, otherwise None."""

    patterns = {
        "MIT": r"MIT License",
        "Apache-2.0": r"Apache License.*Version 2",
        "GPL-3.0": r"GNU GENERAL PUBLIC LICENSE.*Version 3",
        "LGPL-3.0": r"GNU LESSER GENERAL PUBLIC LICENSE.*Version 3",
        "AGPL-3.0": r"GNU AFFERO GENERAL PUBLIC LICENSE.*Version 3",
        "MPL-2.0": r"Mozilla Public License Version 2.0",
        "BSD-2-Clause": r"BSD 2-Clause License",
        "BSD-3-Clause": r"BSD 3-Clause License",
    }

    for spdx_id, pattern in patterns.items():
        if re.search(pattern, license_text, re.DOTALL):
            return spdx_id

    return None


K = TypeVar("K")
V = TypeVar("V")


def inverse_mapping(m: dict[K, V]) -> dict[V, Iterable[K]]:
    """Invert a mapping of unique values to unique keys to a mapping of unique values to sets of keys.

    Examples
    --------
    >>> result = inverse_mapping({1: "a", 2: "b", 3: "a"})
    >>> {k: v for k, v in sorted(result.items())}
    {'a': {1, 3}, 'b': {2}}
    """
    return {v: {k for k, vv in m.items() if vv == v} for v in set(m.values())}
