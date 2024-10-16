import httpx
import pytest

from osswiz.util import classify_license


@pytest.mark.parametrize(
    "spdx_id, full_text_url",
    [
        (
            "MIT",
            "https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/mit.txt",
        ),
        (
            "Apache-2.0",
            "https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/apache-2.0.txt",
        ),
        (
            "GPL-3.0",
            "https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/gpl-3.0.txt",
        ),
        (
            "MPL-2.0",
            "https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/mpl-2.0.txt",
        ),
        (
            "LGPL-3.0",
            "https://raw.githubusercontent.com/github/choosealicense.com/refs/heads/gh-pages/_licenses/lgpl-3.0.txt",
        ),
    ],
)
def test_classify_license(spdx_id: str, full_text_url: str) -> None:
    license_text = httpx.get(full_text_url).text
    assert classify_license(license_text) == spdx_id
