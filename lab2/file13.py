num = int(input("Enter a number (0-19): "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixten", "seventen", "eighteen", "nineteen"]
if 0 <= num < 20:
    print(words[num])
else:
    print("Out of range")