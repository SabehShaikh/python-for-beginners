while True:

    # display menu

    print("Select the Operation: ")

    print("1: Addition")

    print("2: Subtraction")

    print("3: Multiply")

    print("4: Division")

    print("5: Floor Division")

    print("6: Percentage")

    print("7: Exit")

    # take input from user

    choice = input("Enter choice: 1 | 2 | 3 | 4 | 5 | 6 | 7: ")

    if choice == '7':
        print("Exit the calculator")
        break
        

    # user input 

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # operations based on choice:

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")

    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")

    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")

    elif choice == '4':

        if num2 == 0:
            print("Cannot divide by zero")

        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")

    elif choice == '5':

        if num2 == 0:
            print("Cannot divide by zero")

        else:
            print(f"Result: {num1} // {num2} = {num1 // num2}")

    elif choice == '6':
        print(f"{num1} % of {num2} = {num1 * num2 / 100}")

    else:
        print("Invalid input")        

