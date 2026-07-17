# Write a program to check if a number
# is an Armstrong number. 
# An Armstrong number (for a 3-digit number) 
# is an integer such that the sum of the cubes of its digits is equal to the number itself 
# (e.g., 153 = 1^3 + 5^3 + 3^3).

num = 153
temp = num
sum = 0

while num > 0:

    n = num%10
    sum = sum + (n ** 3)

    num = num // 10

if sum == temp:
    print("Yes")
else:
    print("No") 
