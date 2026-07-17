# Write a program to check if a user-entered string contains any numeric digits.
#  Use a for loop to examine each character.

input_string = "Python3"
contains_digit = False

for items in input_string:
    if items.isdigit():
        contains_digit = True
        break
print(f"The string '{input_string}' contains digits: {contains_digit}")
