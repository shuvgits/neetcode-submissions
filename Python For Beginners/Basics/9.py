# Write a program to count the total number of vowels (a, e, i, o, u) 
# present in a given sentence.

sentence = "Learning Python is fun!"
sentence = sentence.lower()
vowels = 'aeiou'
count = 0


for items in sentence:
    if items in vowels:
        count +=1
print(count)
