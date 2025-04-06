# Write a program that takes three diff numbers 
# less than 100  from user and calculate the
# greatest among three numbers...

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 < 100 and number2 < 100 and number3 < 100:
    if number1 > number2 and number1 > number3:
        print(f"Number one {number1} is greater than number two {number2} and number three {number3}")

    elif number2 > number1 and number2 > number3:
        print(f"Number two {number2} is greater than number one {number1} and number three {number3}")

    else:
        print(f"Number three {number3} is greater than number one {number1} and number two {number2}")

else:
    print("Enter numbers less than 100")