x = 1

while x <= 5:
    print("x" , x)
    x = x + 2 # x += 1


count = 1

while count < 5:
    print("Sabeh Shaikh" , count)
    count+=1


# another example:

x = -5
while x <= 1:
    print("Hello" , x)

    x += 1

# Another example:

text = ""

while text != "stop":
    text = input("Enter text: ")

    print(text)


# Another example: 

print("guess a number between 1 to 10")

secret = 5
guess = 0

while guess !=secret:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("You got it")
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

        