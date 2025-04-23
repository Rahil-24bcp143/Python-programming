import math
cx, cy = map(int, input("Enter circle center (x y): ").split())
r = int(input("Enter radius: "))
px, py = map(int, input("Enter point (x y): ").split())
dist = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
if dist < r:
    print("point is inside the circle")
elif dist == r:
    print("point is on the circle")
else:
    print("point is outside the circle")
