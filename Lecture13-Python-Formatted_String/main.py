name = "Alice"
age = 25

# % formatting
message = "My name is %s and I am %d years old." % (name, age)
print(message)

# Another old way: (concatenation)

name = input("your name please? ")
age = input("your age please? ")

print(name + " is " + age + " years old")