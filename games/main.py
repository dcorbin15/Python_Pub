import random
# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep track of the number of guesses
num_guesses = 0

# Start game loop
while True:
    # Get user's guess
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break

    # Check if the guess is too high or too low
    elif guess < number:
        print("Too low! Guess a higher number.")

    else:
        print("Too high! Guess a lower number.")
