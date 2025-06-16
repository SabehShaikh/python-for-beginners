# 2- With user defined functions:

# (a + b)² = a² + 2ab + b²
# write a python program that takes two integers
#  inputs a and b from the User

# create a user defined function named 
# calculate_square() that accepts two arguments
# a and b,
# calculates the result using the above formula and returns the result

# display the result by call the calculate_square() function


print("(a + b)² = a² + 2ab + b²")

def calculate_square(a, b):

    return ( a * a ) + ( 2 * a * b ) + ( b * b )

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = calculate_square(a, b)

print(f"({a} + {b})² = {result}")