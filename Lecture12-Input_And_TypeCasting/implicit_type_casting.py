# Implicit Type Casting--> Python will automatically convert one data type to another

a = 10 #int 
b = 2.5 #float

result = a + b # int + float = float
print("result is:", result)
print("type of result is:", type(result))

x = True #bool --> 1
y = 5 #int

result = x + y # bool + int = int
print("result is:", result)
print("type of result is:", type(result))