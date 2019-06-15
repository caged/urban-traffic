class TrafficFlow:
    def __init__(self, payload):
        self.__raw = payload

    def roadways(self):
        return self.__raw['RWS']
