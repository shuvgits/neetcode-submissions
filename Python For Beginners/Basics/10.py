# Given a list of integers, find and print both the largest 
# and the smallest numbers.

nums = [45, 5, 89, 12, 7, 3]
max = 0
min = 0

for items in nums:
    if max <= items:
        max = items
    else:
        min = items
print(max, min)