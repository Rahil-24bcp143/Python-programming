class Solid:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def cylinder_area(self):
        return 2 * 3.1416 * self.radius * (self.radius + self.height)

    def cylinder_volume(self):
        return 3.1416 * self.radius ** 2 * self.height

s = Solid(15, 65)
print("Surface Area:", s.cylinder_area())
print("Volume:", s.cylinder_volume())