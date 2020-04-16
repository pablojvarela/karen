class Stream:
    def __init__(self, handle):
        self.handle = handle
        self.data = ""
        self.ratio = {}
        self.frequency = {}
        self.ramp = {}

    def read(self, handle):
        # Do something with handle
        return self.data

    def get_ratio(self, data):
        # Calculate ratio
        return self.ratio

    def get_frecuency(self, data):
        # Calculate frequency
        return self.frequency

    def get_ramp(self, data):
        # Calculate ramp
        return self.ramp
