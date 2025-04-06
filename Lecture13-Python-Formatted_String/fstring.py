name = "Alice"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)

# Math operations:

a = 5
b = 3
print(f"Multiplication of {a} and {b} is {a * b}")

x = 10
y = 5
print(f"Sum of {x} and {y} is {x + y} , Multiplication is {x * y}")

pi = 3.141592653589793

print(f"The value of pi is {pi:.2f}") # 2 decimal places

data = {
    "name": "Babar",
    "age": 30
}

print(f"Name: {data['name']}, Age: {data['age']}")

# Multi line strings:

name = "John"
age = 28
bio = f"""
Name: {name}
Age: {age}
"""

print(bio)

# Practice example:

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

print(f"Sum: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")