# Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are
# reversed (e.g., 121, 343).

number = 121
reverse_num = 0
temp = number

while number > 0:

    check = number%10
    reverse_num = (reverse_num * 10) + check
    number = number // 10

if temp == reverse_num:
    print("Palindrone Number")
else:
    print("Not palindrone Number")

