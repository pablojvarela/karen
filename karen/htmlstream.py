import collections
import requests
from karen.karen import stream as stream


class HTMLStream(stream.Stream):
    def __init__(self, url):
        super().__init__(url)

    def read(self, url):
        """
        Fetch an URL and convert HTML content to a list of characters.
        :param url: the URL
        :return: list of characters
        """
        response = requests.get(url)
        return response.content.decode()

