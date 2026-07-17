# Write a function to remove characters from a string starting from index 0 
# up to n and return a new string.

def remove_chars(name, target):
    print(name[target::])

remove_chars("pynative", 4)
remove_chars("pynative", 2)