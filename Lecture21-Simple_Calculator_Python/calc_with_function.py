def menu():

    print("Select operation: ")

    print("1: Addition")

    print("2: Subtraction")

    print("3: Multiply")

    print("4: Division")

    print("5: Exit")

# add

def add(x, y):

    return x + y

# subtract

def sub(x, y):

    return x - y


# multiply

def mul(x, y):

    return x * y

# divide

def div(x, y):

    if y == 0:

        print("Cannot divide by zero")
    
    else: 
        return x / y

# main loop:

while True:

    menu()

    choice = input("Enter choice: 1 | 2 | 3 | 4 | 5: ")

    if choice == '5':
        print("Exit the calculator")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")

    elif choice == '3': 
        print(f"{num1} * {num2} = {mul(num1, num2)}")

    elif choice == '4':
        print(f"{num1} / {num2} = {div(num1, num2)}") 

    else:
        print("Invalid input")       