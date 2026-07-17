# Given a list and an integer k, 
# rotate the list to the left by k positions. 
# For example, if k=2, the first two elements move to the end of the list.

nums = [1, 2, 3, 4, 5]
k = 2

# Perform the rotation k times
for _ in range(k):
    # Remove the first element
    first_element = nums.pop(0)
    # Move it to the end
    nums.append(first_element)

print("Rotated List:", nums)