# Write a program to print the full multiplication table from
# 1 to 10 in a grid format.

for items in range(1,11):

    for j in range(1,11):
        print(items * j, end = "\t")
    print()

