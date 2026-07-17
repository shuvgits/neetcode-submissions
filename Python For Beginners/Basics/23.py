#  Write a program to print the first 
# 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number 
# is the sum of the two preceding ones.

terms = 15
output = []

for items in range(terms):
    if items == 0 or items == 1:
        output.append(items)
    else:
        output.append(output[items - 1] + output[items - 2])
print(output)

