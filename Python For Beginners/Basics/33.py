# Print a downward number pattern where each 
# row starts with a decreasing value.

rows = 5

for items in range(rows,0, -1):
    for p in range(items,0,-1):
        print(p, end = " ")
    print("\n")