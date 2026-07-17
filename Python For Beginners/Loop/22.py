# Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes 
# (increments) with each new row.

rows = 5
ascii_value = 65

for items in range(rows):
    letter = chr(ascii_value + items)
    for j in range(items + 1):
        print(letter, end = " ")
    print()