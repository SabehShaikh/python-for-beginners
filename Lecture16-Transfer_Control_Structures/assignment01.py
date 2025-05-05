# program that keeps asking the user to enter numbers. 
# Stop the loop when the user enters 0

while True:

    num = int(input("Enter a number: "))

    if num == 0:
        break

    print(num)