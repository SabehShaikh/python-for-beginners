# range (start , stop , step)

for i in range(5):
    print(i) # print 0 to 4


for j in range(5, 10):
    print(j) # print 5 to 9


for u in range(10, 0 ,-2):
    print(u)   # print 10 to 1


for name in "Sabeh":
    print(name)

for name in ["Sabeh"]:
    print(name)


fruits = ["apple" , "banana", "mangoes"]

for fruit in fruits:
    print("I like" , fruit)


# finding even number :
numbers = [1,2,3,4,5,6,7,8]

for even in numbers:
    if even % 2 == 0:
        print(f"{even} is even")
