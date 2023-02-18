# accounts.py
# Author: Kealan McGuinness
# Week03 weekly task account number
# import re: re takes in five parameters: the pattern of digits to find in the string, the replacement character, the string or function, the count and the flag, which can ignore the letter case
# choose number of digits to keep, define the masked character
# isdigit to say all characters in the strings are digits
# map used to transform numbers into asterisks
# re.sub replaces the necessary digits with asterisks

import re

ccstring = input('Please enter a 10 digit account number: ')

digitstokeep = 4
maskchar = "*"

ccstringtotal = sum(map(str.isdigit, ccstring))
digitstomask = ccstringtotal - digitstokeep
maskedccstring = re.sub('\d', maskchar, ccstring, digitstomask)

print (maskedccstring)
