# Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax

income = 45000

income1 = ((10000 * 0)+(10000 * 0.1) + ((income-20000)*0.2))
print(income1)