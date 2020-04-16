from karen import stream


class HtmlStream(stream.Stream):
    def __init__(self, url):
        data: list = self.read(url)
        ratio: dict = self.get_ratio(data)
        frequency: dict = self.get_frecuency(data)
        ramp: dict = self.get_ramp(data)

    def read(self, url):
        """
        Fetch an URL and convert HTML content to a list of characters.
        :param url: the URL
        :return: list of characters
        """
        return super().read(url)

    def get_ratio(self, data):
        return super().get_ratio(data)

    def get_frecuency(self, data):
        return super().get_frecuency(data)

    def get_ramp(self, data):
        return super().get_ramp(data)
