# break statement:

x = 1

while x <= 10:
    print(x)

    if x == 5:
        break

    x += 1
 
# output : 1 2 3 4 5

# Another example

for num in range(2,10):
    if num == 7:
        break

    print(num)


x = 1
while x <= 10:
    print(x) # 1 2 3 4 
    x += 1

    if x == 5:
        break


# Another example:

sec_word = "tariff"

counter = 0

while True:

    word = input("Enter the secret word: ").lower()

    if word == sec_word:
        print("You win")
        break

    counter += 1

    if counter == 3:
        print("You lose")
        break

