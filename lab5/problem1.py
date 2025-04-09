import random

odd_nums = [random.randrange(1, 100, 2) for _ in range(5)]
print("Original odd numbers:", odd_nums)

even_nums = [random.randrange(0, 100, 2) for _ in range(4)]
print("Even numbers:", even_nums)

odd_nums[2] = even_nums
print("After replacement:", odd_nums)

flat_list = []
for item in odd_nums:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)
print("Flattened list:", flat_list)

flat_list.sort()
print("Final sorted list:", flat_list)