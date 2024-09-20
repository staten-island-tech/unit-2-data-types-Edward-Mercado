
basevalue = float(input("How much was your meal?"))
tipvalue = (input("How was your service today?"))

if tipvalue == "bad":
    badtotal = basevalue*1.05
    badtotalr = round(badtotal, 2)
    print ("Your total is" + " " + str(badtotalr))
elif tipvalue == "okay":
    okaytotal = basevalue*1.1
    okaytotalr = round(okaytotal, 2)
    print ("Your total is" + " " + str(okaytotalr))
elif tipvalue == "good":
    goodtotal = basevalue*1.15
    goodtotalr = round(goodtotal, 2)
    print ("Your total is" + " " + str(goodtotalr))
elif tipvalue == "spectacular":
    spectaculartotal = basevalue*1.1
    spectaculartotalr = round(spectaculartotal, 2)
    print ("Your total is" + " " + str(spectaculartotal))
else:
    print ("Your total is" + " " + str(basevalue))