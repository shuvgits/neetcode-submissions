#  Write a program to find the 
# largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

num = 75869

max = 0
min = 0

for items in num:

    if max < items:
        max += items
    else:
        min += items

print(f'Max: {max}')
print(f'Min: {min}')