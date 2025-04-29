import random

# Store secret number
SECRET_NUMBER = random.randint(1, 10)

# Ask user to guess
print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Your guess: "))
        if guess == SECRET_NUMBER:
            print("Congratulations! You guessed it!")
            break
        elif guess < SECRET_NUMBER:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Please enter a valid number.")
