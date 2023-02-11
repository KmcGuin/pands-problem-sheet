# accounts.py
# Author: Kealan McGuinness
# Week03 weekly task account number
# import re to use special characters - asterisk
# choose number of digits to keep, define the masked character
# isdigit to say all characters in the strings are digits
# map used to transform numbers into asterisks
# re.sub replaces the necessary digits with asterisks

import re

ccstring = "123456789"
digitstokeep = 4
maskchar = "*"

ccstringtotal = sum(map(str.isdigit, ccstring))
digitstomask = ccstringtotal - digitstokeep
maskedccstring = re.sub('\d', maskchar, ccstring, digitstomask)

print (maskedccstring)
