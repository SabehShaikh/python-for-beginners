# table:

for i in range(1,11):

    result = i * 2
    print(f"2 x {i} = {result}")
   
# table with user input:
num = int(input("Enter a number: "))

for i in range(1,11):

    result = num * i
    print(f"{num} x {i} = {result}")

# check even or odd:

num = int(input("Enter a number between 1 and 100: "))

if num <= 100:

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

else:
    print("Enter a number between 1 and 100")

# check which num is greater:

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 == num2:
    print("Both numbers are equal")
else:
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")

# check which day it is:
choice = input("Enter your choice: M | T | F: ")

if choice == "M" or choice == "m":
    print("Monday")

elif choice == "T" or choice == "t":
    print("Tuesday")

elif choice == "F" or choice == "f":
    print("Friday")

else:
    print("Invalid choice")    

# CHECK Smallest number:

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

smallest = min(n1,n2,n3)

print(f"The smallest number is: {smallest}")