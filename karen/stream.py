class Stream:
    def __init__(self, stream):
        self.process(stream)
        data: list = self.read(stream)
        ratio: dict = self.get_ratio(data)
        frequency: dict = self.get_frecuency(data)
        ramp: dict = self.get_ramp(data)

    def read(self, stream):
        data = []
        return data

    def get_ratio(self, data):
        ratio = {}
        return ratio

    def get_frecuency(self, data):
        frequency = {}
        return frequency

    def get_ramp(self, data):
        ramp = {}
        return ramp
