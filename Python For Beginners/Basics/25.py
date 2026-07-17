# Write a program that takes two separate dictionaries and 
# merges them into one single dictionary.

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

# Modern Python merge (Union Operator)
merged_dict = dict1 | dict2

print(merged_dict)