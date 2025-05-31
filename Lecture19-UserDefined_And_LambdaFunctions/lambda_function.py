# lambda function with one argument:

square = lambda x: x ** 2

print(square(4))

# lambda function with multiple arguments:

add = lambda x , y : x + y

print(f"Addition of 2 and 3 is: {add(2,3)}")

# lambda function with no arguments:

greet = lambda : print("Hello")

greet()

# lambda function with condition:
is_odd = lambda x: x % 2 != 0
result = is_odd(3)
print(result)