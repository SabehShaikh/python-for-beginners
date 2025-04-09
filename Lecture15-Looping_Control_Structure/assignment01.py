# write a program where computer has a fixed secret name of a current pakistani cricket team player (e.g Shaheen Afridi)
# the user should keep guessing the players name untill they guess it correctly
# use a while loop to do this and display the total number of attempts at the end 


print("You have to guess the name of a current Pakistani cricket team player")

secret_name = "Shaheen Afridi"
guess = ""
guess_count = 0

while guess != secret_name:
    guess = input("Enter your guess: ")
    guess_count += 1

    if guess == secret_name:
        print(f"You guessed it in {guess_count} attempts")



