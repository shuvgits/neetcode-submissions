#  Print a multiplication table 
# from 1 to 10 in a formatted grid.

number = range(11)

for items in number[1::]:
    for p in number[1::]:
        print(p * items, end = " ")
    print("\n")