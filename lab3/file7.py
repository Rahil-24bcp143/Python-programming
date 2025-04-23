n = int(input("Enter n: "))
r = int(input("Enter r: "))
fact_n = 1
fact_r = 1
fact_nr = 1

for i in range(1, n+1):
    fact_n *= i
for i in range(1, r+1):
    fact_r *= i
for i in range(1, n-r+1):
    fact_nr *= i

nCr = fact_n // (fact_r * fact_nr)
nPr = fact_n // fact_nr

print("nCr:", nCr)
print("nPr:", nPr)