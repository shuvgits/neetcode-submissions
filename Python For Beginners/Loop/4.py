# Write a program that accepts a 
# number from the user and calculates the sum of all numbers 
# from 1 up to that number.

num = int(input("Enter number:"))
sum = 0

for items in range(num + 1):
    sum += items
print(f'Sum is: {sum}')
