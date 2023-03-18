# squareroot.py
# Author: Kealan McGuinness
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.



num = float(input('Please enter a positive number: '))
sq_root = round(num ** 0.5, 1) 
print(f'The square root of {num} is approx. {sq_root}')

'''
def newton_method(number, number_iters = 500):
    a = float(number) 
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number

num = input('Please enter a positive number: ')
print(f'The square root of {num} is approx {newton_method(num)}')
'''
