import re
from collections.abc import Iterable
from typing import TypeVar


def classify_license(license_text: str) -> str | None:
    """Attempt to classify a license based on its text. Returns the SPDX identifier if recognized, otherwise None."""

    patterns = {
        "MIT": r"MIT License",
        "MIT-0": r"MIT No Attribution",
        "Apache-2.0": r"Apache License.*Version 2",
        "MPL-2.0": r"Mozilla Public License Version 2\.0",
        "EPL-2.0": r"Eclipse Public License - v 2\.0",
        "Unlicense": r"This is free and unencumbered software released into the public domain",
        "WTFPL": r"DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE",
        "BSL-1.0": r"Boost Software License - Version 1\.0",
        "EUPL-1.2": r"EUROPEAN UNION PUBLIC LICENCE v\. 1\.2",
        "Zlib": r"zlib License",
        # GPL licenses
        "GPL-3.0": r"GNU GENERAL PUBLIC LICENSE.*Version 3",
        "GPL-2.0": r"GNU GENERAL PUBLIC LICENSE.*Version 2",
        "LGPL-3.0": r"GNU LESSER GENERAL PUBLIC LICENSE.*Version 3",
        "LGPL-2.1": r"GNU LESSER GENERAL PUBLIC LICENSE.*Version 2.1",
        "AGPL-3.0": r"GNU AFFERO GENERAL PUBLIC LICENSE.*Version 3",
        # BSD licenses
        "0BSD": r"BSD Zero Clause License",
        "BSD-2-Clause": r"BSD 2-Clause License",
        "BSD-3-Clause": r"BSD 3-Clause License",
        "BSD-3-Clause-Clear": r"The Clear BSD License",
        "ISC": r"ISC License",
        # AI/ML licenses
        "BigScience-OpenRAIL-M": r"BigScience Open RAIL-M License",
        "CreativeML-OpenRAIL-M": r"CreativeML Open RAIL-M",
        # Creative Commons licenses
        "CC0-1.0": r"CC0 1.0 Universal",
        "CC-BY-4.0": r"Creative Commons Attribution 4.0",
        "CC-BY-SA-4.0": r"Creative Commons Attribution-ShareAlike 4.0",
        "CC-BY-NC-4.0": r"Creative Commons Attribution-NonCommercial 4.0",
        "CC-BY-ND-4.0": r"Creative Commons Attribution-NoDerivatives 4.0",
        "CC-BY-NC-SA-4.0": r"Creative Commons Attribution-NonCommercial-ShareAlike 4.0",
        "CC-BY-NC-ND-4.0": r"Creative Commons Attribution-NonCommercial-NoDerivatives 4.0",
        # Open Data Commons licenses
        "ODbL-1.0": r"ODC Open Database License \(ODbL\)",
        "ODC-By-1.0": r"ODC Attribution License \(ODC-By\)",
        "PDDL-1.0": r"Public Domain Dedication and License \(PDDL\)",
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
