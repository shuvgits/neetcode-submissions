# Write a program to remove all duplicate 
# values from a list using a loop, maintaining 
# the original order of elements.

original = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = []

for num in original:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List:", unique_list)

