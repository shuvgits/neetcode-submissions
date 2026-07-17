# Write a program that takes an
# integer n and prints the cube of every 
# number from 1 to n in the format Current Number is : 1 and the cube is 1.

input_number = 6

for items in range(1, input_number + 1):
    cube = items ** 3
    print(f'Current Number is: {items} and the cube is {cube}')

