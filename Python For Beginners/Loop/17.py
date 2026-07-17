# Write a program to use a loop to find the 
# factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.

num = 5
factorial = 1

for items in range(num, 0, -1):
    factorial = factorial * items

print(factorial)

