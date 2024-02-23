import random

def play_guess_the_number():
    number = random.randint(1, 1000)
    attempts = 0

    while True:
        guess = int(input("Guess my number: "))
        attempts += 1

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
