# Create a countdown timer that starts from a given number and counts 
# down to zero using a while loop.

import time

count = 5

while count > 0:
    print(count)
    # Pause the program for 1 second
    time.sleep(1)
    # Decrement the counter
    count -= 1

print("Blast off!")