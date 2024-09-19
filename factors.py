x  = int(input("Please type a number: "))

factors = {1}  

for factor in range(2, x + 1):
    if x % factor == 0:
        factors.add(factor)

print(factors)