# bank.py
# Author: Kealan McGuinness
# Week02 task 02 banks
# int to convert string into an integer
# use formattedfloat to change numbers into euro
# I haven't figured out how to have the Euro value appear correctly yet. Will return to this.

x = input("Enter first amount (in cent): ")
y = input("Enter second amount (in cent): ")
amount = int(x) + int(y)

formattedfloat = str("The sum is: €{:,.2f}".format(amount))

print(formattedfloat)



