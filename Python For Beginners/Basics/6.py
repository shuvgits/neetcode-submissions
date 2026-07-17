# Write a program that calculates the factorial of a given
# number (e.g., 5!) using a for loop.

number = int(input('Number:'))
factorial = 1

for items in range(1, number + 1):
        factorial = factorial * items
print(f'The factorial is: {factorial}')
