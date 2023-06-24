import random
from number_guess_art import *

total_lives = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

difficulty_test = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_test == "hard":
    total_lives = 5
if difficulty_test == "easy":
    total_lives = 10

print(f"You have {total_lives} attempts remaining to guess the number")

correct_number = False
while not correct_number:
    random_guess = int(input("Make a guess: "))
    total_lives -= 1

    if random_guess > random_number:
        print(f"You have {total_lives} attempts remaining to guess the number")
        print("Too high")
        print("Guess again")
    elif random_guess < random_number:
        print(f"You have {total_lives} attempts remaining to guess the number")
        print("Too low")
        print("Guess again")
    else:
        correct_number = True
        print("Congratulations! You guessed the correct number.")
