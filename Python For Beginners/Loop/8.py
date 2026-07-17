# Given a list of numbers, use a loop to count how many times a specific
# number (e.g., 10) appears.

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
sum = 0

for items in list1:
    if items == target:
        sum += 1
print(f'{target} appears {sum} times')