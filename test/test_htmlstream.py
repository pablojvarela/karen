import pytest
import requests

from karen import htmlstream

URL = requests.get("https://en.wikipedia.org/wiki/User_Datagram_Protocol")


@pytest.mark.htmlstream
def test_read():
    data = htmlstream.HtmlStream.read(URL)
    assert data is list, "Failed to fetch URL."


@pytest.mark.htmlstream
def test_get_ratio():
    assert False


def test_get_frecuency():
    assert False


@pytest.mark.htmlstream
def test_get_ramp():
    assert False

