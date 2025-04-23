a = int(input("Enter first : "))
b = int(input("Enter second : "))
c = int(input("Enter third : "))
if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

print("largest:", largest, "smallest:", smallest)