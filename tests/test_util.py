import httpx
import pytest

from osswiz.util import classify_license


def _choosealicense_url(license: str) -> str:
    return f"https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/{license}.txt"


def _cc_url(license: str) -> str:
    if license == "zero":
        return "https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt"
    return f"https://creativecommons.org/licenses/{license}/4.0/legalcode.txt"


@pytest.mark.parametrize(
    "spdx_id, full_text_url",
    [
        ("MIT", _choosealicense_url("mit")),
        ("MIT-0", _choosealicense_url("mit-0")),
        ("Apache-2.0", _choosealicense_url("apache-2.0")),
        ("MPL-2.0", _choosealicense_url("mpl-2.0")),
        ("EPL-2.0", _choosealicense_url("epl-2.0")),
        ("Unlicense", "https://unlicense.org/UNLICENSE"),
        ("WTFPL", "http://www.wtfpl.net/txt/copying/"),
        ("BSL-1.0", _choosealicense_url("bsl-1.0")),
        (
            "EUPL-1.2",
            "https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%20EN.txt",
        ),
        ("Zlib", _choosealicense_url("zlib")),
        # GPL licenses
        ("GPL-3.0", _choosealicense_url("gpl-3.0")),
        ("GPL-2.0", _choosealicense_url("gpl-2.0")),
        ("LGPL-3.0", _choosealicense_url("lgpl-3.0")),
        ("LGPL-2.1", _choosealicense_url("lgpl-2.1")),
        ("AGPL-3.0", _choosealicense_url("agpl-3.0")),
        # BSD licenses
        ("0BSD", _choosealicense_url("0bsd")),
        ("BSD-2-Clause", _choosealicense_url("bsd-2-clause")),
        ("BSD-3-Clause", _choosealicense_url("bsd-3-clause")),
        ("BSD-3-Clause-Clear", _choosealicense_url("bsd-3-clause-clear")),
        # Creative Commons licenses
        ("CC0-1.0", _cc_url("zero")),
        ("CC-BY-4.0", _cc_url("by")),
        ("CC-BY-SA-4.0", _cc_url("by-sa")),
        ("CC-BY-NC-4.0", _cc_url("by-nc")),
        ("CC-BY-ND-4.0", _cc_url("by-nd")),
        ("CC-BY-NC-SA-4.0", _cc_url("by-nc-sa")),
        ("CC-BY-NC-ND-4.0", _cc_url("by-nc-nd")),
        # Open Data Commons licenses
        ("ODbL-1.0", "https://opendatacommons.org/licenses/odbl/odbl-10.txt"),
        (
            "ODC-By-1.0",
            "https://opendatacommons.org/licenses/by/odc_by_1.0_public_text.txt",
        ),
        ("PDDL-1.0", "https://opendatacommons.org/licenses/pddl/pddl-10.txt"),
    ],
)
def test_classify_license(spdx_id: str, full_text_url: str) -> None:
    license_text = httpx.get(full_text_url).text

    if "choosealicense" in full_text_url:
        # Split at --- since the license text follows the frontmatter in choosealicense repo
        license_text = license_text.split("---", 2)[-1].strip()

    assert classify_license(license_text) == spdx_id, license_text
