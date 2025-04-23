x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter second point (x2 y2): ").split())
x3, y3 = map(int, input("Enter third point (x3 y3): ").split())
if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
    print("points are collinear")
else:
    print("points are not collinear")