# program that input three numbers and check
# whether a number is divisible by two , three or five

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 % 2 == 0 or num1 % 3 == 0 or num1 % 5 == 0:
    print(f"{num1} is divisible by 2, 3 or 5")
else:
    print(f"{num1} is NOT divisible by 2, 3 or 5")

if num2 % 2 == 0 or num2 % 3 == 0 or num2 % 5 == 0:
    print(f"{num2} is divisible by 2, 3 or 5")
else:
    print(f"{num2} is NOT divisible by 2, 3 or 5")

if num3 % 2 == 0 or num3 % 3 == 0 or num3 % 5 == 0:
    print(f"{num3} is divisible by 2, 3 or 5")
else:
    print(f"{num3} is NOT divisible by 2, 3 or 5")
