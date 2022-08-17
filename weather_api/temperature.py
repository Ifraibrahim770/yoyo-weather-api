import statistics


class Temperature:
    """Model Class for the Temperature Data"""

    def __init__(self, city, days, data):
        self.city = city
        self.days = days
        self.maximum = round(max(data), 2)
        self.minimum = round(min(data), 2)
        self.median = round(statistics.median(data), 2)
        self.average = round(statistics.mean(data), 2)
