# squareroot.py
# Author: Kealan McGuinness
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.



num = float(input('Please enter a positive number: '))
sq_root = round(num ** 0.5, 1) 
print(f'The square root of {num} is approx. {sq_root}')


## def isqrt(n):
#    x = n
 #   y = (x + 1) // 2
  #  while y < x:
   #     x = y
    #    y = (x + n // x) // 2
    # return x

# answer = input("Please enter a positive number: ")
# print(f"The square root of {answer} is approx."))
