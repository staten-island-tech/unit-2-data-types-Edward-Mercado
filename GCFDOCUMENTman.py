numuno=int(input("Input a number."))
numdos=int(input("Input another numnber."))

factors2 = {1}
factors1 = {1}
factors3 = {1}

for factor1 in range(2, numdos + 1):
    if numuno % factor1 == 0:
        factors1.add(factor1)

for factor2 in range(2, numdos + 1):
    if numdos % factor2 == 0:
        factors2.add(factor2)
             
for x in range(2, factors1):
    if x in factors1 and factors2:
        factors3.add(x)
print(factors3)