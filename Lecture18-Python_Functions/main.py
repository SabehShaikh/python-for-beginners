items = [10,20,30]

print(len(items))
print(type(items))
print(sum(items)) # 10 + 20 + 30
print(max(items)) # 30
print(min(items)) # 10

# round > rounds the number

print(round(2.12))
print(round(2.52))
print(round(2.4))

# isinstance > checks the type
print(isinstance(1,int))
print(isinstance(1.0,int))
print(isinstance(1.0,float))

# any > checks if any of the items are true

print(any([True, False, False]))
print(any([False, False, False]))

# all > checks if all of the items are true

print(all([True, True, True]))
print(all([True, False, True]))

# divmod > returns the quotient and remainder

print(divmod(10,3)) # (quotient, remainder)
print(divmod(9,3))

a = int(input("Input dividend: "))
b = int(input("Input divisor: "))

result = divmod(a,b)
print(result)

# pow > raises a number to a power

print(pow(2,3))

