#  Given a list of integers, move all even numbers to the beginning of the list 
# and all odd numbers to the end.

numbers = [1, 2, 3, 4, 5, 6]
evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

# Merging lists
result = evens + odds
print("Segregated List:", result)