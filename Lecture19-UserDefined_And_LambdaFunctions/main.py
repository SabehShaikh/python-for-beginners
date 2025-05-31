def add_num(a , b):

    return a + b

print(add_num(1,2))

def eid_wish(name):

    return f"Eid Mubarak {name}"

print(eid_wish("Sabeh"))

print(eid_wish("Ali"))

# sq of number:
def sqr(x):

    return x ** 2

print(sqr(6))

# non-parametrized function:
def greet():

    print("Hello")

greet()

# area of rectangular:

def area(length, width):

    return length * width

print(f"Area of rectangle is: {area(4,5)}")

# default parameter: (optional parameter)

def user(name = "Unknown"):

    print(f"Hello {name}")

user("Ali")

user()