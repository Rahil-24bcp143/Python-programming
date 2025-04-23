class Shape:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

sq = Shape(5)
print("Area:", sq.area())
print("Perimeter:", sq.perimeter())