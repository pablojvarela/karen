import pytest
import requests
from karen import htmlstream

URL = "https://en.wikipedia.org/wiki/User_Datagram_Protocol"


@pytest.fixture
def create_htmlstream():
    return htmlstream.HtmlStream(URL)


@pytest.mark.htmlstream
def test_read(create_htmlstream):
    htmlstream.HtmlStream.read(create_htmlstream, URL)
    assert type(create_htmlstream.data) == str, "HtmlStream.data is not string."


