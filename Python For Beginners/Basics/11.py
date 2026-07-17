# Write a script that takes a list containing duplicate items and returns 
# a new list with only unique elements.

data = [1, 2, 2, 3, 4, 4, 4, 5]
unique = ''
unique1 = list(set(data))

for items in str(data):
    if items in unique:
        pass
    else:
        unique += items + ' '

print(unique)
print(unique1)
