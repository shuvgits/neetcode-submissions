#  Print a downward half-pyramid 
# pattern using stars (*).

number = range(6)

for p in number[::-1]:
    print(" * " * p, end=" ")
    print("\n")
