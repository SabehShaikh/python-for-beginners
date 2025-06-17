# ZeroDivisionError:

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    result = a / b
except ZeroDivisionError:
    print("You cannot divide by zero")    

else: # runs when no error in try
    print("The result is: ", result)    

# ValueError:
try: 
    num = int(input("Enter any integer: "))

except ValueError:
    print("Not a valid integer") 

else: 
    print(f"You entered: {num}")    

# IndexError:
list = ["Free" , "CS" , "Academy"]
index = int(input("Enter index: "))

try:
    print(f"Element at index {index} is: {list[index]}")

except IndexError:
    print("Error: Index out of range")    
           

# RaiseException:
age = float(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age is valid")

except ValueError:
    print("Error: Age cannot be negative")

else:
    print(f"Your age is: {age}")                


# MultipleExceptions:
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ValueError:
    print("Please enter valid numbers")  

except (ZeroDivisionError):
    print("You cannot divide by zero")

else:
    print(f"The result of {a} / {b} is: {result}")    
