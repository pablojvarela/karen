from karen.stream import Stream


class SelfspyStream(Stream):

    def read(self, stream):
        return super().read(stream)

    def get_ratio(self, data):
        return super().get_ratio(data)

    def get_frecuency(self, data):
        return super().get_frecuency(data)

    def get_ramp(self, data):
        return super().get_ramp(data)