# Write a program to find all prime 
# numbers up to 20, but only print every second (alternate) 
# prime number found.

Limit = 20
number = range(100)
final = []

for items in range(Limit):
    output = []
    for p in number[1:items + 1]:
        q = items%p
        
        if q == 0:
            output.append(p)
    
    if output == [1, items]:
        final.append(items)

print(final[::2])

