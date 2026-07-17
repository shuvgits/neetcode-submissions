# Iterate through the first 10 numbers (0–9). In each iteration, 
# print the current number, the previous number, 
# and their sum.

numbers = range(10)
sum = 0
previous = 0

for items in numbers:
        if items == 0:
            previous = 0
            sum = items + previous
        else:
             previous = items - 1 
             sum = items + previous
        print(f'C: {items}, P: {previous}, S:{sum}')
