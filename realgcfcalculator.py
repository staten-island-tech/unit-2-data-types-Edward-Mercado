number1 = int(input("Provide the first number."))
number2 = int(input("Provide the second number."))

commonfactors = {1}
for x in range(2, number1):
    if number1 % x == 0 and number2 % x == 0:
        commonfactors.add(x)

gcf = max(commonfactors)
print (gcf)