N = int(input("Enter N: "))
a, b = 0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()