# if statement

age = 20
if age >= 18:
    print("You are an adult")

print("END")    

x = 20
if (x>15):
    print("10 is less than 15")

print("I am not in if block")    

# If else statement:
a = 100

if a>50:
    print("Execute this block if condition is true")

else:
    print("Execute this block if condition is false") 

       
# Guess whether i will press a or b:

choice = input("Enter your choice: A or B ")

if choice == "A" or choice == "a":
    print("You pressed A")

else:
    print("You pressed B")   

# if elif else statement:
    
temp = 34

if temp > 35:
    print("It is hot outside")

elif temp>20:
    print("It is warm outside")

else:
    print("It is cold outside")        


# Another example:

x = 12
y = 50

if x == y:
    print("x is equal to y")

elif x > y:
    print("x is greater than y")

else:
    print("x is less than y")

# Nested if:
num = 16

if num > 10:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

