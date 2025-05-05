# continue statement: skips the current iteration of the loop

for num in range(1,10):
    if num == 6:
        continue

    print(num) 


n = 1
while n < 5:
    if n == 2:
        n += 1
        continue

    print("Hello Pakistan")

    n += 1

# numbers which are divisible by 2 (even),
#  we don't want to print

for i in range(8):
    if i % 2 == 0:
        continue

    print(i)

# looping through a string
for letter in "Hello":

    if letter == "l":
        continue

    print(letter) # H e o

num = [1,-2,3,-4,5,-6]
for n in num:
    if n < 0:
        continue

    print(n)