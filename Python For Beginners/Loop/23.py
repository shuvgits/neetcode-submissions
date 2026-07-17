# Print a 5*5 square of stars where the middle is 
# empty, leaving only the border.

size = 5

for i in range(size):

    for j in range(size):
        
        if i == 0 or i == size - 1:
            print("*", end = ' ')
        elif j == 0 or j == size - 1:
            print("*", end = ' ')
        else:
            print( " ", end = " ")
    print()
            
