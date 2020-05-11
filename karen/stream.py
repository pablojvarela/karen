import numpy as np
import collections
import logging
logging.basicConfig(level=logging.DEBUG)


class Stream:
    def __init__(self, handle):
        """
        Initialize the Stream object.
        This is the base class for all stream types.
        :param handle: a string. For subclasses of different stream types, it is a handle to the stream.
        """
        self.data = self.read(handle)
        self._counter = collections.Counter(self.data)
        self._frequencies = np.array([x for x in self._counter.values()])

        self.topten = self._counter.most_common(10)
        self.topfreq = self._counter.most_common(1)[0][1]
        self.lowfreq = self._counter.most_common()[-1][1]
        self.avgfreq = (self.topfreq + self.lowfreq) / 2

        self.georamp = np.geomspace(self._frequencies.min(), self._frequencies.max(), self._frequencies.size)
        self.lowergeoramp = self.georamp[0:int(self.georamp.size/2)]
        self.uppergeoramp = self.georamp[int(self.georamp.size/2):self.georamp.size]

        self.lineramp = np.linspace(self._frequencies.min(), self._frequencies.max(), self._frequencies.size)

    def read(self, handle):
        """
        Read stream into a string for parsing.
        Override this method for new stream types.
        :param handle: an entry point for the stream. For example,
        for HtmlStream the handle is the URL from where to fetch content.
        :return: a string representation of the stream
        """
        return handle

