#Explicit type casting--> manually convert one data type to another

# first_num = input("Enter first number:")
# second_num = input("Enter second number:")
# sum = first_num + second_num # str + str = concatenation
# print("result is:", sum)
# print("type of result is:", type(sum)) # str

# To solve this:

first_num = int(input("Enter first number:"))
second_num = int(input("Enter second number:"))
sum = first_num + second_num # int + int = int
print("result is:", sum)
print("type of result is:", type(sum)) # int

# another way:
first_num = input("Enter first number:")
second_num = input("Enter second number:")
sum = int(first_num) + int(second_num)
print("result is:", sum)
print("type of result is:", type(sum)) 

# Another example:

birth_year = input("Enter your birth year:")
your_age = 2025 - int(birth_year)
print("Your age is:", your_age)

# Another example:

price = float(input("Enter price: "))
print("Double the price: " , price * 2)

# Another example: (boolean)

flag = bool(input("Enter 1 for True, 0 for False: "))

print("Boolean value: " , flag)

# Another example: (str to int)

my_string = "20"

print(my_string)
print(int(my_string)*2)
