# Given a Python list, use a loop to print only the elements that are located at odd index 
# positions (index 1, 3, 5, etc.).

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
output = []

for i, items in enumerate(my_list):
    if i%2!=0:
        print(items)