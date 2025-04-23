num = int(input("Enter number: "))

#prime 
is_prime = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# perfect
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
is_perfect = (sum_factors == num)

# armstrong
temp = num
sum_armstrong = 0
while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** len(str(num))
    temp //= 10
is_armstrong = (sum_armstrong == num)

#palindrome
is_palindrome = (str(num) == str(num)[::-1])

# automorphic
is_automorphic = (str(num**2).endswith(str(num)))

print("Prime:", is_prime)
print("Perfect:", is_perfect)
print("Armstrong:", is_armstrong)
print("Palindrome:", is_palindrome)
print("Automorphic:", is_automorphic)