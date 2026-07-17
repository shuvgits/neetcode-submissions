# Write a function called exponent(base, exp) that returns an integer value of the base raised 
# to the power of the exponent.

def exponent(base,exp):
    product = base
    for items in range(exp-1):
        product = product * base
    return product

print(exponent(2,0))