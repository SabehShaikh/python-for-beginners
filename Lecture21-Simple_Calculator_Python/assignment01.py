# 1- Without using user defined functions:

# (a + b)² = a² + 2ab + b²

# write a python program that takes two integers
#  inputs a and b from the User
# calculate (a + b) ^ 2 by using the above formula
# display the reult 

print("(a + b)² = a² + 2ab + b²")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = ( a * a ) + ( 2 * a * b ) + ( b * b )

print(f"({a} + {b})² = {result}")


