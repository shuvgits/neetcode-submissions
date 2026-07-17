# Print the following pattern where each row contains a number repeated a 
# specific number of times based on its value.

numbers = range(5)
for items in numbers:
    for p in numbers[:items]:
        print(items, end=" ")
    print("\n")