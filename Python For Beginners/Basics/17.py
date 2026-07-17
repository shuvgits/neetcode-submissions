# Create a new list from two given lists such that the new list contains odd numbers from the first list and 
# even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for items in list1:
    if items%2 != 0:
        list3.append(items)

for items in list2:
    if items%2 == 0:
        list3.append(items)

print(list3)

