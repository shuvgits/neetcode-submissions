# Write a program to check if 
# a given number is a palindrome (reads the same forwards and backwards).

i = input("Enter Number:")

def r(x):
    p = x[::-1]

    if x == p:
        print(f'Number {x} is a palindrome number')
    else:
        print(f'Number {x} is not a palindrome number')


r(i)