# Write a program to extract each digit from 
# an integer in the reverse order.

number = 7536
print("Given Number:", number)

while number > 0:
    # Get the last digit
    digit = number % 10
    
    # Remove the last digit from number
    number = number // 10
    
    print(digit, end=" ")