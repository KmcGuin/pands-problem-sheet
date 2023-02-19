# collatz.py
# Author: Kealan McGuinness
# Week04 weekly task - asks the user to input any positive integer and outputs the successive values of the following calculation.
# 
# Line 12 - use // float division as / returned decimals
# .append to return the results in a list form
# Line 23 - asterisk is used if you don't know how many arguments will be passed through the function. 
# corrected to remove commas in the answer


number = int(input('Enter a positive integer: '))

answer = [number]
while number > 1:
    if number%2 == 0:
        number = number//2

        answer.append(number)

    else:
        number = (number*3) + 1
        answer.append(number)
    
print(*answer)



