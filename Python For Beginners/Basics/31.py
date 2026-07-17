# Create a dictionary where the keys
# are numbers from 1 to 10 and the values are the squares of those
# numbers (e.g., 2: 4, 3: 9).

n = range(10)
f = {}

for items in n[1:]:
    f[items] = items * items
print(f)
    
