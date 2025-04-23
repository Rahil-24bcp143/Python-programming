class Weather:
    def __init__(self, params):
        self.params = params

    def __contains__(self, item):
        return item in self.params

w = Weather(["Rain", "Humidity", "Wind"])
print("Rain" in w)
print("Snow" in w)