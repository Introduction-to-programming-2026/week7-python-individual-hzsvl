import random

secret = random.randint(1, 10)
guesses = 0

guess = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    guesses += 1
    
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    guess = int(input("Try again: "))

guesses += 1

print(f"Congratulations! You guessed it in {guesses} attempts.")
