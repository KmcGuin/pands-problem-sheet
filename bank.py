# bank.py
# Author: Kealan McGuinness
# Week02 task 02 banks
# int to convert string into an integer
# use formattedfloat to change numbers into euro


x = input("Enter first amount (in cent): ")
y = input("Enter second amount (in cent): ")
amount = int(x) + int(y)
newamount = amount/100

formattedfloat = str("The sum is: €{:,.2f}".format(newamount))

print(formattedfloat)



