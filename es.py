# es.py
# Author: Kealan McGuinness
#Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

#The program should take the filename from an argument on the command line.


FILENAME = 'ulysses.txt'

import sys
n = len(sys.argv)

print(sys.argv[0], FILENAME)


FILENAME = 'ulysses.txt'
with open(FILENAME, 'r') as f:
    data = f.read()

def lettercount (FILENAME, letter):
    with open(FILENAME, 'r') as f:
        text = f.read()
    return text.count(letter)

ans = lettercount('ulysses.txt', 'e')
print('The letter e appears this many times:',ans)