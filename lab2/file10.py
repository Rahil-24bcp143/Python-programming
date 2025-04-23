l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area = l * b
perimeter = 2 * (l + b)
if area > perimeter:
    print("Area is greater")
else:
    print("Perimeter is greater")
