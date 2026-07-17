# Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

number1 = int(input("Enter the value of the first number:"))
number2 = int(input("Enter the value of the second number:"))


if number1 * number2 <= 1000:
    print(number1 * number2)
else:
    print(number1 + number2)