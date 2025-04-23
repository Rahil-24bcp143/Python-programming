class Date:
    def __init__(self, d, m, y):
        self.date = [d, m, y]

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
print("Dates are equal." if d1 == d2 else "Dates are not equal.")