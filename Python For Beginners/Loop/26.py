# Given a list of numbers, 
# create a new list where each element is the sum of all elements from the original list up to that position.

value = [1,2,5,4]
sum = 0
output = []

for i in value:
    sum = sum + i
    output.append(sum)
print(f'Cumulative Sum: {output}')



