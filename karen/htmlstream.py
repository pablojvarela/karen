import requests
from karen import stream


class HtmlStream(stream.Stream):
    def __init__(self, url):
        super().__init__(url)

    def read(self, url):
        """
        Fetch an URL and convert HTML content to a list of characters.
        :param url: the URL
        :return: list of characters
        """
        r = requests.get(url)
        self.data = r.content.decode()
        return
